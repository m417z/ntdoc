'use strict';

(function () {
    run();

    function run() {
        try {
            initSearch();
        } catch (e) {
            console.error(e);
        }

        try {
            addControlButtons();
        } catch (e) {
            console.error(e);
        }

        try {
            if (typeof tippy !== 'undefined') {
                // https://stackoverflow.com/a/66726233
                const calculateScrollbarWidth = () => {
                    document.documentElement.style.setProperty('--scrollbar-width', (window.innerWidth - document.documentElement.clientWidth) + 'px');
                };
                // Recalculate on resize.
                window.addEventListener('resize', calculateScrollbarWidth);
                // Recalculate on dom load.
                document.addEventListener('DOMContentLoaded', calculateScrollbarWidth); 
                // Recalculate on load (assets loaded as well).
                window.addEventListener('load', calculateScrollbarWidth);

                tippy('[title]', {
                    content(reference) {
                        const title = reference.getAttribute('title');
                        reference.removeAttribute('title');
                        return title;
                    },
                    theme: 'code-preview',
                    maxWidth: 'calc(100vw - var(--scrollbar-width) - 10px)',
                });
            }
        } catch (e) {
            console.error(e);
        }
    }

    function initSearch() {
        var DataProvider = function () {
            this.availableItems = null;
            this.items = null;
        };
        DataProvider.prototype.load = function () {
            var deferred = Q.defer();
            var self = this;
            if (this.availableItems) {
                deferred.resolve();
            } else {
                $.ajax({
                    url: 'ident-to-id.json'
                }).done(function (data) {
                    self.availableItems = [];
                    Object.keys(data).sort().forEach(function (item) {
                        self.availableItems.push({
                            id: data[item],
                            name: item
                        });
                    });
                    self.items = self.availableItems;

                    deferred.resolve();
                }).fail(function (jqXHR, textStatus) {
                    var msg = textStatus;
                    if (jqXHR.status) {
                        msg += ': status code ' + jqXHR.status;
                    }
                    alert(msg);
                });
            }
            return deferred.promise;
        };
        DataProvider.prototype.filter = function (search) {
            var searchArray = search.toLowerCase().split(/\s+/);
            if (searchArray.length > 0) {
                this.items = this.availableItems.filter(function (item) {
                    var itemNameLowerCase = item.name.toLowerCase();
                    return searchArray.every(function (word) {
                        return itemNameLowerCase.indexOf(word) !== -1;
                    });
                });
            } else {
                this.items = this.availableItems;
            }
        };
        DataProvider.prototype.get = function (firstItem, lastItem) {
            return this.items.slice(firstItem, lastItem);
        };
        DataProvider.prototype.size = function () {
            return this.items.length;
        };
        DataProvider.prototype.identity = function (item) {
            return item.id;
        };
        DataProvider.prototype.displayText = function (item, extended) {
            if (item) {
                return item.name;
                //return extended ? item.name + ' (' + item.id + ')' : item.name;
            } else {
                return '';
            }
        };
        DataProvider.prototype.noSelectionText = function () {
            return 'Search docs';
        };
        var dataProvider = new DataProvider();

        $('#ntdoc-search-select').virtualselect({
            dataProvider: dataProvider,
            onSelect: function (item) {
                window.location = item.id;
            },
        }).virtualselect('load');
    }

    function addControlButtons() {
        const codeElementsContainer = document.querySelector('.ntdoc-code-elements');
        if (!codeElementsContainer) {
            return;
        }

        const controlButtonsContainer = document.createElement('div');
        controlButtonsContainer.classList.add('ntdoc-code-control-buttons');

        const buttonCopy = document.createElement('button');
        buttonCopy.classList.add('ntdoc-code-control-button-autohide');
        buttonCopy.textContent = 'Copy';
        buttonCopy.addEventListener('click', () => {
            const codeElement = Array.from(
                codeElementsContainer.querySelectorAll(':scope > .ntdoc-code-element')
            ).filter((e) => e.style.display !== 'none')[0];
            const code = codeElement.querySelector('.ntdoc-code-intro').textContent +
                codeElement.querySelector('.ntdoc-code-body').textContent;
            navigator.clipboard.writeText(code);

            const previousText = buttonCopy.textContent;
            buttonCopy.textContent = '✅';
            buttonCopy.disabled = true;
            setTimeout(() => {
                buttonCopy.textContent = previousText;
                buttonCopy.disabled = false;
            }, 500);
        });
        controlButtonsContainer.append(buttonCopy);

        const codeElements = codeElementsContainer.querySelectorAll(':scope > .ntdoc-code-element');
        if (codeElements.length > 1) {
            let currentBlockIndex = 0;

            const buttonLeft = document.createElement('button');
            buttonLeft.textContent = '⬅️';
            buttonLeft.title = 'Previous definition';
            buttonLeft.disabled = true;

            const buttonRight = document.createElement('button');
            buttonRight.textContent = '➡️';
            buttonRight.title = 'Next definition';

            buttonLeft.addEventListener('click', () => {
                codeElements[currentBlockIndex].style.display = 'none';
                currentBlockIndex--;
                codeElements[currentBlockIndex].style.display = 'block';
                buttonLeft.disabled = currentBlockIndex === 0;
                buttonRight.disabled = currentBlockIndex === codeElements.length - 1;
            });

            buttonRight.addEventListener('click', () => {
                codeElements[currentBlockIndex].style.display = 'none';
                currentBlockIndex++;
                codeElements[currentBlockIndex].style.display = 'block';
                buttonLeft.disabled = currentBlockIndex === 0;
                buttonRight.disabled = currentBlockIndex === codeElements.length - 1;
            });

            controlButtonsContainer.append(buttonLeft, buttonRight);
        }

        codeElementsContainer.append(controlButtonsContainer);
    }
})();
