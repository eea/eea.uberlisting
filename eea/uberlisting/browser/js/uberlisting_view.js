/* readCookie and createCookie from Plone cookie_functions.js */ 
/*global window, jQuery */ 
/* Events
*/
window.Uberlisting = {};
window.Uberlisting.Events = {};
window.Uberlisting.Events.Success = 'Success';

jQuery(function($, window) {
        "use strict";
        var $smart_view_switch = $('#smart-view-switch');
        var faceted = $("#faceted-form").length;

        var smart_view = $(window.Uberlisting.Events).bind(window.Uberlisting.Events.Success, function(evt) {
            var href = window.location.href;
            if(href.indexOf('folder_tabs_view') !== -1 ) {
                // run logic for tabs from eea-tabs.js
                window.EEA.eea_tabs();
                return;
            }
            if(href.indexOf('folder_accordion_view') !== -1 ) {
                // run logic for tabs from eea-accordion.js
                window.EEA.eea_accordion();
                return;
            }
        });

        var markSelectedButton = function () {
            var smartTemplate = $.bbq.getState('smartTemplate');
            var $smart_view_switch = $("#smart-view-switch");
            $smart_view_switch.find('.selected').removeClass('selected');
            $smart_view_switch.find('a').each(function(i) {
                var $this = $(this);
                var templateID = $this.data().templateid;
                if (templateID === smartTemplate) {
                    $this.addClass('selected');
                }
            });
        };

        var loadCookieSetttings =  function() {
            if ($.bbq.getState('smartTemplate') === undefined && window.readCookie('smartTemplate')) {
                $.bbq.pushState({
                    'smartTemplate': window.readCookie('smartTemplate')
                });
            }
        };

        var loadContent = function() {
            var $smart_view_content = $('#smart-view-content');
            $smart_view_content.html('<img src="ajax-loader.gif" />');
            var url = $.param.querystring($.bbq.getState('smartTemplate'), $.param.querystring());
            url = url + '?ajax_load=1';
            var EEA = window.EEA;
            $.get(url, function(data) {
                var $data = $(data).find('#content-core').contents();
                $smart_view_content.html($data);
                $(window.Uberlisting.Events).trigger(window.Uberlisting.Events.Success);
                var listing_a = $smart_view_content.find('.listingBar a');

                if (listing_a.length) {
                    listing_a.each(function(i) {
                        var batchQueryString = $.param.querystring(this.href);
                        var newUrl = $.param.querystring(window.location.href, batchQueryString);
                        this.href = newUrl;
                    });
                }
            }, 'html');
        };

        $("#smart-view-switch").delegate('a', 'click', function(evt) {
            var smartTemplate = $(this).data().templateid;
            $.bbq.pushState({
                'smartTemplate': smartTemplate
            });
            // #3370 - IE7 does not pick up on hash changes
            var ie6or7 = $.browser.msie && (parseInt($.browser.version, 10) <= 7);
            if (faceted) {
                if (window.Faceted.Window.width && ie6or7) {
                    window.Faceted.Query = window.Faceted.URLHandler.hash2query(window.location.hash);
                    $(window.Faceted.Events).trigger(window.Faceted.Events.QUERY_CHANGED);
                    window.Faceted.Form.do_form_query();
                }

            }
            window.createCookie('smartTemplate', smartTemplate);
            evt.preventDefault();
        });


        if (faceted) {
            $(window.Faceted.Events).bind('FACETED-AJAX-QUERY-SUCCESS', function(evt){
                var smart_view = $("#smart-view-content");
                if (smart_view.length) {
                    markSelectedButton();
                    smart_view.find('.listingBar').remove();
                    $(window.Uberlisting.Events).trigger(window.Uberlisting.Events.Success);
                }
            });

        }

        if ($smart_view_switch.length) {
            loadCookieSetttings();
            $(window).bind('hashchange', function(e) {
                // If faceted navigation is enabled, we don't have to make our own
                // AJAX request.
                markSelectedButton();
                if(!faceted){
                    loadContent();
                }
            });
        }

})(jQuery, window);
