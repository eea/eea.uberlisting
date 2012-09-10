/* readCookie and createCookie from Plone cookie_functions.js */ 
/*global window, jQuery */ 
/* Events
*/
window.Uberlisting = {};
window.Uberlisting.Events = {};
window.Uberlisting.Events.Success = 'Success';

jQuery(document).ready(function($) {
    "use strict";
    var $uber_view_switch = $('#uber-view-switch');
    var faceted = $("#faceted-form").length;
    var ie6or7 = $.browser.msie && (parseInt($.browser.version, 10) <= 7);

    // bind our success handler only if we have EEA object
    if (window.EEA) {
        $(window.Uberlisting.Events).bind(window.Uberlisting.Events.Success, function(evt) {
            var uberTemplate = $.bbq.getState('uberTemplate');
            if (uberTemplate === 'folder_tabs_view') {
                // run logic for tabs from eea-tabs.js
                window.EEA.eea_tabs();
                return;
            }
            if (uberTemplate === 'folder_accordion_view') {
                // run logic for tabs from eea-accordion.js
                window.EEA.eea_accordion();
                return;
            }
            if (uberTemplate === 'gallery_view') {
                $('#galleryView').eeaGalleryView();
            }
        });
    }

    var markSelectedButton = function () {
        var uberTemplate = $.bbq.getState('uberTemplate');
        var $uber_view_switch = $("#uber-view-switch");
        $uber_view_switch.find('.selected').removeClass('selected');
        $uber_view_switch.find('a').each(function(i) {
            var $this = $(this);
            var templateID = $this.data().templateid;
            if (templateID === uberTemplate) {
                $this.addClass('selected');
            }
        });
    };

    var loadCookieSetttings =  function() {
        if ($.bbq.getState('uberTemplate') === undefined && window.readCookie('uberTemplate')) {
            $.bbq.pushState({
                'uberTemplate': window.readCookie('uberTemplate')
            });
        }
    };

    var loadContent = function() {
        var $uber_view_content = $('#uber-view-content');
        $uber_view_content.html('<img src="ajax-loader.gif" />');
        var url = $.param.querystring($.bbq.getState('uberTemplate'), $.param.querystring());
        url = url + '?ajax_load=1';
        var EEA = window.EEA;
        $.get(url, function(data) {
            var $data = $(data).find('#content-core').contents();
            $uber_view_content.html($data);
            var listing_a = $uber_view_content.find('.listingBar a');

            if (listing_a.length) {
                listing_a.each(function(i) {
                    var batchQueryString = $.param.querystring(this.href);
                    var newUrl = $.param.querystring(window.location.href, batchQueryString);
                    this.href = newUrl;
                });
            }

            $(window.Uberlisting.Events).trigger(window.Uberlisting.Events.Success);
        }, 'html');
    };

    $("#content").delegate('#uber-view-switch a', 'click', function(evt) {
        var uberTemplate = $(this).data().templateid;
        $.bbq.pushState({
            'uberTemplate': uberTemplate
        });
        if (faceted) {
            // #3370 - IE7 does not pick up on hash changes
            if (ie6or7) {
                window.Faceted.Query = window.Faceted.URLHandler.hash2query(window.location.hash);
                $(window.Faceted.Events).trigger(window.Faceted.Events.QUERY_CHANGED);
                window.Faceted.Form.do_form_query();
            }
        }
        window.createCookie('uberTemplate', uberTemplate);
        evt.preventDefault();
    });

    if (faceted) {
        loadCookieSetttings();
        $(window.Faceted.Events).bind('FACETED-AJAX-QUERY-SUCCESS', function(evt){
            var uber_view = $("#uber-view-content");
            if (uber_view.length) {
                markSelectedButton();
                uber_view.find('.listingBar').remove();
                $(window.Uberlisting.Events).trigger(window.Uberlisting.Events.Success);
            }
        });
    }

    if ($uber_view_switch.length) {
        loadCookieSetttings();
        $(window).bind('hashchange', function(e) {
            // If faceted navigation is enabled, we don't have to make our own
            // AJAX request.
            markSelectedButton();
            if (!faceted) {
                loadContent();
            }
        });
    }

});
