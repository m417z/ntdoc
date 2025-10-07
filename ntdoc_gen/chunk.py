"""Chunk data structures and operations."""

import re
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Dict, List, Tuple


class ChunkOrigin(IntEnum):
    PHNT = auto()
    MSDN_DDI = auto()
    MSDN_WIN32 = auto()
    MSDN_DRIVER_FUZZY = auto()
    MSDN_WIN32_FUZZY = auto()


@dataclass
class Chunk:
    origin: ChunkOrigin
    code_url: str
    idents: List[str]
    before: List[Tuple[str, str]]
    intro: str
    body: str
    after: List[str]


def remove_redundant_forward_declaration_chunks(chunks: List[Chunk]) -> List[Chunk]:
    def is_forward_declaration(chunk: Chunk) -> bool:
        body = chunk.body.rstrip('\n')
        return re.fullmatch(r'(typedef )?(struct|union|enum) (\w+).*;(\s*//.*)?', body) is not None

    result: List[Chunk] = []

    for chunk in chunks:
        if is_forward_declaration(chunk):
            # Conflicts with MSDN docs.
            if chunk.idents[0] == 'PIRP':
                continue

            idents_unique = set(chunk.idents)

            for chunk_other in chunks:
                if chunk_other is chunk or is_forward_declaration(chunk_other):
                    continue

                for ident in list(idents_unique):
                    if ident in chunk_other.idents:
                        idents_unique.remove(ident)

            if idents_unique == set():
                continue

        result.append(chunk)

    return result


def organize_idents_to_ids(chunks: List[Chunk]) -> Dict[str, str]:
    ident_to_id: Dict[str, str] = {}
    id_special_cases: Dict[str, str] = {
        'FSINFOCLASS': 'FS_INFORMATION_CLASS',
        'PERFINFO_TRACE_ENTRY': 'PERFINFO_TRACE_HEADER',
        'WMI_DISKIO_READWRITE': 'ETW_DISKIO_READWRITE_V3',
        'WMI_DISKIO_FLUSH_BUFFERS': 'ETW_DISKIO_FLUSH_BUFFERS_V3',
        'MOFRESOURCEINFOA': 'MOFRESOURCEINFO',
        'MOFRESOURCEINFOW': 'MOFRESOURCEINFO',
    }
    id_update_from_to_collisions: Dict[str, str] = {
        # Collides with function WinStationShadow.
        'WINSTATIONSHADOW': 'winstationshadow-2',
        # Collides with function ConsoleControl.
        'CONSOLECONTROL': 'consolecontrol-2',
        # Collides with function OEMMemoryUsage.
        'OEMMEMORYUSAGE': 'oemmemoryusage-2',
        # Collides with function ReadControlSpace.
        'READCONTROLSPACE': 'readcontrolspace-2',
        # Collides with function ReadControlSpace64.
        'READCONTROLSPACE64': 'readcontrolspace64-2',
        # Collides with function SearchMemory.
        'SEARCHMEMORY': 'searchmemory-2',
        # Collides with size_t (lowercase).
        'SIZE_T': 'size_t-2',
        # Collides with RtlXxxToSizeT.
        'RtlDWord64ToSIZET': 'rtldword64tosizet-2',
        'RtlDWordLongToSIZET': 'rtldwordlongtosizet-2',
        'RtlInt16ToSIZET': 'rtlint16tosizet-2',
        'RtlInt32ToSIZET': 'rtlint32tosizet-2',
        'RtlInt64ToSIZET': 'rtlint64tosizet-2',
        'RtlInt8ToSIZET': 'rtlint8tosizet-2',
        'RtlIntPtrToSIZET': 'rtlintptrtosizet-2',
        'RtlIntToSIZET': 'rtlinttosizet-2',
        'RtlLong64ToSIZET': 'rtllong64tosizet-2',
        'RtlLongLongToSIZET': 'rtllonglongtosizet-2',
        'RtlLongPtrToSIZET': 'rtllongptrtosizet-2',
        'RtlLongToSIZET': 'rtllongtosizet-2',
        'RtlPtrdiffTToSIZET': 'rtlptrdiffttosizet-2',
        'RtlShortToSIZET': 'rtlshorttosizet-2',
        'RtlSSIZETToSIZET': 'rtlssizettosizet-2',
        'RtlUInt64ToSIZET': 'rtluint64tosizet-2',
        'RtlULong64ToSIZET': 'rtlulong64tosizet-2',
        'RtlULongLongToSIZET': 'rtlulonglongtosizet-2',
        # Collides with RtlSizeTXXX.
        'RtlSIZETAdd': 'rtlsizetadd-2',
        'RtlSIZETMult': 'rtlsizetmult-2',
        'RtlSIZETSub': 'rtlsizetsub-2',
        # Collides with RtlSizeTToXXX.
        'RtlSIZETToByte': 'rtlsizettobyte-2',
        'RtlSIZETToChar': 'rtlsizettochar-2',
        'RtlSIZETToDWord': 'rtlsizettodword-2',
        'RtlSIZETToInt': 'rtlsizettoint-2',
        'RtlSIZETToInt16': 'rtlsizettoint16-2',
        'RtlSIZETToInt32': 'rtlsizettoint32-2',
        'RtlSIZETToInt64': 'rtlsizettoint64-2',
        'RtlSIZETToInt8': 'rtlsizettoint8-2',
        'RtlSIZETToIntPtr': 'rtlsizettointptr-2',
        'RtlSIZETToLong': 'rtlsizettolong-2',
        'RtlSIZETToLong64': 'rtlsizettolong64-2',
        'RtlSIZETToLongLong': 'rtlsizettolonglong-2',
        'RtlSIZETToLongPtr': 'rtlsizettolongptr-2',
        'RtlSIZETToPtrdiffT': 'rtlsizettoptrdifft-2',
        'RtlSIZETToShort': 'rtlsizettoshort-2',
        'RtlSIZETToSSIZET': 'rtlsizettossizet-2',
        'RtlSIZETToUChar': 'rtlsizettouchar-2',
        'RtlSIZETToUInt': 'rtlsizettouint-2',
        'RtlSIZETToUInt16': 'rtlsizettouint16-2',
        'RtlSIZETToUInt32': 'rtlsizettouint32-2',
        'RtlSIZETToUInt8': 'rtlsizettouint8-2',
        'RtlSIZETToULong': 'rtlsizettoulong-2',
        'RtlSIZETToUShort': 'rtlsizettoushort-2',
        'RtlSIZETToWord': 'rtlsizettoword-2',
        'SMBIOS_PROCESSOR_FAMILY_ULTRASPARC_Iii': 'smbios_processor_family_ultrasparc_iii-1',
        'SMBIOS_PROCESSOR_FAMILY_ULTRASPARC_III': 'smbios_processor_family_ultrasparc_iii-2',
    }
    id_update_from_to = id_update_from_to_collisions.copy()

    for chunk in chunks:
        id = chunk.idents[0]
        id = re.sub(r'(struct|union|enum) (.*)', r'\2-\1', id)

        for ident in chunk.idents:
            if ident not in ident_to_id:
                ident_to_id[ident] = id
                continue

            id1 = ident_to_id[ident]
            id2 = id

            if id1 in id_special_cases and id2 == id_special_cases[id1]:
                id_update_from_to[id1] = id_special_cases[id1]
            elif id2 in id_special_cases and id1 == id_special_cases[id2]:
                id_update_from_to[id2] = id_special_cases[id2]
            else:
                assert id1 == id2, (ident, id1, id2)

    # ZwAbc and NtAbc are the same, assign the same id.
    for k in ident_to_id:
        if k.startswith('Zw'):
            nt_k = 'Nt' + k[2:]
            assert nt_k in ident_to_id, (k, nt_k)
            ident_to_id[k] = ident_to_id[nt_k]

    for k in ident_to_id:
        if ident_to_id[k] in id_update_from_to:
            ident_to_id[k] = id_update_from_to[ident_to_id[k]]

    id_lower_case_mapping = {}
    for k in ident_to_id:
        id_lower_case = ident_to_id[k].lower()
        id_original_case = ident_to_id[k]

        if id_lower_case in id_lower_case_mapping:
            assert id_lower_case_mapping[id_lower_case] == id_original_case, (
                f'Different case for {id_original_case}: {id_lower_case_mapping[id_lower_case]} vs {id_original_case}')
        else:
            id_lower_case_mapping[id_lower_case] = id_original_case

        ident_to_id[k] = id_lower_case
        assert re.fullmatch(r'[a-z0-9_]+(-(struct|union|enum))?', ident_to_id[k]) or ident_to_id[k] in id_update_from_to_collisions.values(), ident_to_id[k]

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        for ident in chunk.idents[1:]:
            assert ident_to_id[ident] == id, (ident, ident_to_id[ident], id)

    return ident_to_id
