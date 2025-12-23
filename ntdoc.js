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
            addDescriptionSwitching();
        } catch (e) {
            console.error(e);
        }

        try {
            if (typeof anchors !== 'undefined') {
                anchors.add('.ntdoc-description-selected :is(h1, h2, h3, h4, h5, h6)');
            }
        } catch (e) {
            console.error(e);
        }

        // Highlight.js, must run before tippy to allow tooltips in code.
        try {
            if (typeof hljs !== 'undefined') {
                highlightCode();
            }
        } catch (e) {
            console.error(e);
        }

        try {
            if (typeof tippy !== 'undefined') {
                addTooltips();
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
            if (searchArray.length > 1 || (searchArray.length === 1 && searchArray[0] !== '')) {
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
        // Wrap the button to allow tippy to work.
        // https://github.com/atomiks/tippyjs/issues/286
        const wrapperForButtonCopy = document.createElement('span');
        wrapperForButtonCopy.append(buttonCopy);
        let copiedTooltip = typeof tippy !== 'undefined' ? tippy(wrapperForButtonCopy, {
            content: 'Copied',
            theme: 'ntdoc',
            trigger: 'manual',
        }) : null;
        buttonCopy.classList.add('ntdoc-code-control-button-autohide');
        buttonCopy.textContent = 'Copy';
        buttonCopy.addEventListener('click', () => {
            const codeElement = Array.from(
                codeElementsContainer.querySelectorAll(':scope > .ntdoc-code-element')
            ).filter((e) => e.style.display !== 'none')[0];
            const code = codeElement.querySelector('.ntdoc-code-intro').textContent +
                codeElement.querySelector('.ntdoc-code-body').textContent;
            navigator.clipboard.writeText(code);

            buttonCopy.disabled = true;
            copiedTooltip?.show();
            copiedTooltip?.setProps({
                trigger: 'mouseenter focus',
            });
            setTimeout(() => {
                buttonCopy.disabled = false;
                copiedTooltip?.hide();
                copiedTooltip?.setProps({
                    trigger: 'manual',
                });
            }, 500);
        });
        controlButtonsContainer.append(wrapperForButtonCopy);

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

            if (typeof tippy !== 'undefined') {
                tippy(controlButtonsContainer.querySelectorAll('[title]'), {
                    content(reference) {
                        const title = reference.getAttribute('title');
                        reference.removeAttribute('title');
                        return title;
                    },
                    theme: 'ntdoc',
                });
            }
        }

        codeElementsContainer.append(controlButtonsContainer);
    }

    function addDescriptionSwitching() {
        const descriptionsContainer = document.querySelector('.ntdoc-descriptions');
        if (!descriptionsContainer) {
            return;
        }

        const titleElements = descriptionsContainer.querySelectorAll('.ntdoc-description-title');
        const descriptionElements = descriptionsContainer.querySelectorAll('.ntdoc-description');

        // Need at least 2 descriptions to show a switcher.
        if (titleElements.length < 2 || descriptionElements.length < 2) {
            return;
        }

        // Create the select element.
        const selectElement = document.createElement('select');
        selectElement.className = 'ntdoc-description-selector';

        // Find currently selected description index.
        let selectedIndex = 0;
        for (let i = 0; i < descriptionElements.length; i++) {
            if (descriptionElements[i].classList.contains('ntdoc-description-selected')) {
                selectedIndex = i;
                break;
            }
        }

        // Populate select options from title elements.
        titleElements.forEach((titleElement, index) => {
            const option = document.createElement('option');
            option.value = index;
            option.textContent = titleElement.textContent.trim();
            if (index === selectedIndex) {
                option.selected = true;
            }
            selectElement.appendChild(option);
        });

        // Add change event listener.
        selectElement.addEventListener('change', (event) => {
            const newIndex = parseInt(event.target.value);

            // Remove selected class from all descriptions.
            descriptionElements.forEach((desc) => {
                desc.classList.remove('ntdoc-description-selected');
            });

            // Add selected class to the chosen description.
            if (descriptionElements[newIndex]) {
                descriptionElements[newIndex].classList.add('ntdoc-description-selected');
            }
        });

        descriptionsContainer.prepend(selectElement);
    }

    function highlightCode() {
        const cssSelector = [
            'pre code[class^="language-"]',
            'pre code[class*=" language-"]',
            '.ntdoc-code-header',
            '.ntdoc-code-intro',
            '.ntdoc-code-body',
            '.ntdoc-code-footer',
        ].join(', ');

        hljs.configure({
            cssSelector,
            ignoreUnescapedHTML: true,
        });

        hljs.addPlugin(hljsMergeHTMLPlugin());

        const blocks = document.querySelectorAll(cssSelector);
        blocks.forEach(hljs.highlightElement);
    }

    function addTooltips() {
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
            theme: 'ntdoc code-preview',
            maxWidth: 'calc(100vw - var(--scrollbar-width) - 10px)',
        });
    }
})();

// https://github.com/highlightjs/highlight.js/issues/2889
function hljsMergeHTMLPlugin() {
  'use strict';

  var originalStream;

  /**
   * @param {string} value
   * @returns {string}
   */
  function escapeHTML(value) {
    return value
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#x27;');
  }

  /* plugin itself */

  /** @type {HLJSPlugin} */
  const mergeHTMLPlugin = {
    // preserve the original HTML token stream
    "before:highlightElement": ({ el }) => {
      originalStream = nodeStream(el);
    },
    // merge it afterwards with the highlighted token stream
    "after:highlightElement": ({ el, result, text }) => {
      if (!originalStream.length) return;

      const resultNode = document.createElement('div');
      resultNode.innerHTML = result.value;
      result.value = mergeStreams(originalStream, nodeStream(resultNode), text);
      el.innerHTML = result.value;
    }
  };

  /* Stream merging support functions */

  /**
   * @typedef Event
   * @property {'start'|'stop'} event
   * @property {number} offset
   * @property {Node} node
   */

  /**
   * @param {Node} node
   */
  function tag(node) {
    return node.nodeName.toLowerCase();
  }

  /**
   * @param {Node} node
   */
  function nodeStream(node) {
    /** @type Event[] */
    const result = [];
    (function _nodeStream(node, offset) {
      for (let child = node.firstChild; child; child = child.nextSibling) {
        if (child.nodeType === 3) {
          offset += child.nodeValue.length;
        } else if (child.nodeType === 1) {
          result.push({
            event: 'start',
            offset: offset,
            node: child
          });
          offset = _nodeStream(child, offset);
          // Prevent void elements from having an end tag that would actually
          // double them in the output. There are more void elements in HTML
          // but we list only those realistically expected in code display.
          if (!tag(child).match(/br|hr|img|input/)) {
            result.push({
              event: 'stop',
              offset: offset,
              node: child
            });
          }
        }
      }
      return offset;
    })(node, 0);
    return result;
  }

  /**
   * @param {any} original - the original stream
   * @param {any} highlighted - stream of the highlighted source
   * @param {string} value - the original source itself
   */
  function mergeStreams(original, highlighted, value) {
    let processed = 0;
    let result = '';
    const nodeStack = [];

    function selectStream() {
      if (!original.length || !highlighted.length) {
        return original.length ? original : highlighted;
      }
      if (original[0].offset !== highlighted[0].offset) {
        return (original[0].offset < highlighted[0].offset) ? original : highlighted;
      }

      /*
      To avoid starting the stream just before it should stop the order is
      ensured that original always starts first and closes last:

      if (event1 == 'start' && event2 == 'start')
        return original;
      if (event1 == 'start' && event2 == 'stop')
        return highlighted;
      if (event1 == 'stop' && event2 == 'start')
        return original;
      if (event1 == 'stop' && event2 == 'stop')
        return highlighted;

      ... which is collapsed to:
      */
      return highlighted[0].event === 'start' ? original : highlighted;
    }

    /**
     * @param {Node} node
     */
    function open(node) {
      /** @param {Attr} attr */
      function attributeString(attr) {
        return ' ' + attr.nodeName + '="' + escapeHTML(attr.value) + '"';
      }
      // @ts-ignore
      result += '<' + tag(node) + [].map.call(node.attributes, attributeString).join('') + '>';
    }

    /**
     * @param {Node} node
     */
    function close(node) {
      result += '</' + tag(node) + '>';
    }

    /**
     * @param {Event} event
     */
    function render(event) {
      (event.event === 'start' ? open : close)(event.node);
    }

    while (original.length || highlighted.length) {
      let stream = selectStream();
      result += escapeHTML(value.substring(processed, stream[0].offset));
      processed = stream[0].offset;
      if (stream === original) {
        /*
        On any opening or closing tag of the original markup we first close
        the entire highlighted node stack, then render the original tag along
        with all the following original tags at the same offset and then
        reopen all the tags on the highlighted stack.
        */
        nodeStack.reverse().forEach(close);
        do {
          render(stream.splice(0, 1)[0]);
          stream = selectStream();
        } while (stream === original && stream.length && stream[0].offset === processed);
        nodeStack.reverse().forEach(open);
      } else {
        if (stream[0].event === 'start') {
          nodeStack.push(stream[0].node);
        } else {
          nodeStack.pop();
        }
        render(stream.splice(0, 1)[0]);
      }
    }
    return result + escapeHTML(value.substr(processed));
  }

  return mergeHTMLPlugin;

}
