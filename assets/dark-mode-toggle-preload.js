function getStylesheetTagsForDarkModeToggle(lightModeHref, darkModeHref) {
    'use strict';

    const PREFERS_COLOR_SCHEME = 'prefers-color-scheme';
    const LIGHT = 'light';
    const DARK = 'dark';
    const ALL = 'all';
    const NOT_ALL = 'not all';
    const NAME = 'dark-mode-toggle';

    let mode = null;
    try {
        mode = localStorage.getItem(NAME);
    } catch (e) { }

    let lightCSSMedia = `(${PREFERS_COLOR_SCHEME}: ${LIGHT})`;
    let darkCSSMedia = `(${PREFERS_COLOR_SCHEME}: ${DARK})`;

    switch (mode) {
        case LIGHT:
            lightCSSMedia += ', ' + ALL;
            darkCSSMedia += ' and ' + NOT_ALL;
            break;

        case DARK:
            darkCSSMedia += ', ' + ALL;
            lightCSSMedia += ' and ' + NOT_ALL;
            break;
    }

    return `
        <link rel="stylesheet" href="${lightModeHref}" media="${lightCSSMedia}">
        <link rel="stylesheet" href="${darkModeHref}" media="${darkCSSMedia}">
    `;
}
