 (() => {
        const elements = document.querySelectorAll('.js-date-format');
        const cache = [];
        elements.forEach((el, i) => {
            const dateString = el.innerHTML.toString();
            const STARTED = new Date(dateString);
            update(el, STARTED, i);
        })

        function getParamsObj(value) {
            const obj = {
                interval: null,
                type: 'date',
            }
            if (value < 60 * 1000) {
                obj.interval = 1000;
                obj.type = 'second';
            }
            if (value >= 60 * 1000 && value < 60 * 60 * 1000) {
                obj.interval = 60 * 1000;
                obj.type = 'minute';
            }
            if (value >= 60 * 60 * 1000 && value < 24 * 60 * 60 * 1000) {
                obj.interval = 60 * 60 * 1000;
                obj.type = 'hour';
            }
            return obj;
        }

        function getString(type, value) {
            let string = value;
            switch (type) {
                case 'second': {
                    string = string + ' second';
                    break;
                }
                case 'minute': {
                    string = string + ' minute';
                    break;
                }
                case 'hour': {
                    string = string + ' hour';
                    break;
                }
                default: {
                    string = null;
                }
            }
            if (string !== null) {
                if (value > 1) {
                    string = string + 's';
                }
                string = string + ' ago'
            }
            return string;
        }

        function saveCache(el, STARTED, paramsObj, indexCache) {
            if (paramsObj.interval !== null) {
                cache[indexCache] = {
                    type: paramsObj.type,
                    interval: window.setInterval(() => {
                        update(el, STARTED, indexCache);
                    }, paramsObj.interval)
                }
            }
        }

        function update(el, STARTED, indexCache) {
            console.log('updating ' + indexCache);
            const NOW = new Date();
            const diff = (NOW.getTime() - STARTED.getTime());
            const paramsObj = getParamsObj(diff);
            const value = parseInt(diff / paramsObj.interval, 10).toFixed(0);
            const stringValue = getString(paramsObj.type, value);
            if (stringValue !== null) {
                el.innerHTML = stringValue;
            } else {
                el.innerHTML = STARTED.toISOString();

            }
            if (cache[indexCache]) {
                if (cache[indexCache].type !== paramsObj.type) {
                    window.clearInterval(cache[indexCache].interval);
                    saveCache(el, STARTED, paramsObj, indexCache);
                }
            } else {
                saveCache(el, STARTED, paramsObj, indexCache);
            }
        }
    })()