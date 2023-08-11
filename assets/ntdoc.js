'use strict';

(function () {
    run();

    function run() {
        initSearch();
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
})();
