/* readCookie and createCookie from Plone cookie_functions.js */ 
jQuery(document).ready(function($) {
    var $smart_view_switch = $('#smart-view-switch');
    // hide from display menu the smart view if faceted navigation is enabled
    // #5080
    var smart_view_action = $("#smart_view");
    if (smart_view_action.length && $("#faceted_settings").length) {
        smart_view_action.parent().hide();
    }

    if ($smart_view_switch.length) {
       var $smart_view_switch_li = $smart_view_switch.find('li');
       var markSelectedButton = function () {
            var smartTemplate = $.bbq.getState('smartTemplate');
            $smart_view_switch.find('.selected').removeClass('selected');
            $smart_view_switch_li.each(function(i) {
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
                if(url.indexOf('tabs') !== -1 ) {
                    // run logic for tabs from eea-tabs.js
                    EEA.eea_tabs();
                }
                if(url.indexOf('accordion') !== -1 ) {
                    // run logic for tabs from eea-accordion.js
                    EEA.eea_accordion();
                }
                var listing_a = $smart_view_content.find('.listingBar a');
                if (listing_a.length) {
                    listing_a.each(function(i) {
                        var batchQueryString = $.param.querystring(this.href);
                        var newUrl = $.param.querystring(location.href, batchQueryString);
                        this.href = newUrl;
                    });
                }
            }, 'html');
        };

        $smart_view_switch_li.bind('click', function() {
            var smartTemplate = $(this).data().templateid;
            $.bbq.pushState({
                'smartTemplate': smartTemplate
            });
            // #3370 - IE7 does not pick up on hash changes
            var ie6or7 = $.browser.msie && (parseInt($.browser.version, 10) <= 7);
            if (window.Faceted) {
                if (window.Faceted.Window.width && ie6or7) {
                    window.Faceted.Query = window.Faceted.URLHandler.hash2query(location.hash);
                    $(window.Faceted.Events).trigger(window.Faceted.Events.QUERY_CHANGED);
                    window.Faceted.Form.do_form_query();
                }
            }
            window.createCookie('smartTemplate', smartTemplate);
        });

        loadCookieSetttings();

        $(window).bind('hashchange', function(e) {
            // If faceted navigation is enabled, we don't have to make our own
            // AJAX request.
            if (window.Faceted) {
                if (!window.Faceted.Window.width && ($.bbq.getState('smartTemplate') !== undefined)) {
                    markSelectedButton();
                    loadContent();
                }
            }
        }).trigger('hashchange');
    }
});
