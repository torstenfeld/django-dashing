/* global $, Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('current_valuation_widget', 'Number', {
    getData: function () {
        $.extend(this.data, {
            title: 'Current Valuation',
            more_info: 'In billions',
            updated_at: 'Last updated at 14:10',
            detail: '64%',
            value: '$35'
        });
    }
});

dashboard.addWidget('buzzwords_widget', 'List', {
    getData: function () {
        $.extend(this.data, {
            title: 'Buzzwords',
            more_info: '# of times said around the office',
            updated_at: 'Last updated at 18:58',
            data: [{label: 'Exit strategy', value: 24},
                   {label: 'Web 2.0', value: 12},
                   {label: 'Turn-key', value: 2},
                   {label: 'Enterprise', value: 12},
                   {label: 'Pivoting', value: 3},
                   {label: 'Leverage', value: 10},
                   {label: 'Streamlininess', value: 4},
                   {label: 'Paradigm shift', value: 6},
                   {label: 'Synergy', value: 7}]
        });
    }
});

dashboard.addWidget('convergence_widget', 'Graph', {
    getData: function () {
        $.extend(this.data, {
            title: 'Convergence',
            value: '41',
            more_info: '',
            data: [ 
                    { x: 0, y: 40 }, 
                    { x: 1, y: 49 }, 
                    { x: 2, y: 38 }, 
                    { x: 3, y: 30 }, 
                    { x: 4, y: 32 }
                ]
            });
    }
});

dashboard.addWidget('weather_widget', 'Weather', {
    WOEID: 2367749 //Bozeman
});

dashboard.addWidget('weather_widget', 'Weather', {
    WOEID: 44418 //London
});

dashboard.addWidget('weather_widget', 'Weather', {
    WOEID: 2295420 //Bangalore
});

dashboard.addWidget('knob_widget', 'Knob', {
    data: {
        title: 'Twitter Followers?',
        more_info: 'for @thiswasnotreal?',
        value: 0
    },
    interval: 5000, //30 min
    getData: function () {
        var self = this;

        $.extend(self.data, {
            value: 23,
            data: {
                angleArc: 250,
                fgColor: '#90ee90',
                angleOffset: -125,
                displayInput: true,
                displayPrevious: false,
                step: 1,
                min: 0,
                max: 10000,
                readOnly: true
            }
        });
        self.data.value = Math.floor((Math.random() * 10000) + 1);;
        self.data.updated_at = lastUpdate();

        home.publish('knob/render');
        $('.dashing-knob').trigger('change');
    }
});

dashboard.addWidget('number_change_test_widget', 'Numberchange', {
    data: {
        title: '',
        value: 4,
        previous: 2,
    },
    getData: function () {
        var self = this;
        $.extend(self.data, {
            title: 'Number change test',
            value: 5,
            previous: 7,
            updated_at: '6.1.2015 12:40:43'
        });
        home.publish('number_change_test_widget/render');
    }
});
