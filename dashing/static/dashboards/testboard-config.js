/* global $, Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

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
