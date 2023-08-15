(function () {
    'use strict';

    const PREFERS_COLOR_SCHEME = 'prefers-color-scheme';
    const MEDIA = 'media';
    const LIGHT = 'light';
    const DARK = 'dark';
    const LINK_REL_STYLESHEET = 'link[rel=stylesheet]';
    const ALL = 'all';
    const NOT_ALL = 'not all';
    const NAME = 'dark-mode-toggle';
    const darkCSS = document.querySelectorAll(
        `${LINK_REL_STYLESHEET}[${MEDIA}*=${PREFERS_COLOR_SCHEME}][${MEDIA}*="${DARK}"]`,
    );
    const lightCSS = document.querySelectorAll(
        `${LINK_REL_STYLESHEET}[${MEDIA}*=${PREFERS_COLOR_SCHEME}][${MEDIA}*="${LIGHT}"]`,
    );
    switch (localStorage.getItem(NAME)) {
        case LIGHT:
            lightCSS.forEach((link) => {
                link.media += ', ' + ALL;
                link.disabled = false;
            });
            darkCSS.forEach((link) => {
                link.media += ' and ' + NOT_ALL;
                link.disabled = true;
            });
            break;
        case DARK:
            darkCSS.forEach((link) => {
                link.media += ', ' + ALL;
                link.disabled = false;
            });
            lightCSS.forEach((link) => {
                link.media += ' and ' + NOT_ALL;
                link.disabled = true;
            });
            break;
    }
})();
