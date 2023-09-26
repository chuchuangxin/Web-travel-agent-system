/**
 * Main scripts file
 */
(function($) {
  'use strict';
  /* Define some variables */
  var app = $('.app'),
    searchState = false,
    menuState = false;

  function toggleMenu() {
    if (menuState) {
      app.removeClass('move-left move-right');
      setTimeout(function() {
        app.removeClass('offscreen');
      }, 150);
    } else {
      app.addClass('offscreen move-right');
    }
    menuState = !menuState;
  }

  /******** Open messages ********/
  $('[data-toggle=message]').on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    app.toggleClass('message-open');
  });

  /******** Open contact ********/
  $('[data-toggle=contact]').on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    app.toggleClass('contact-open');
  });

  /******** Toggle expanding menu ********/
  $('[data-toggle=expanding]').on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    app.toggleClass('expanding');
  });

  /******** Card collapse control ********/
  $('[data-toggle=card-collapse]').on('click', function(e) {
    var parent = $(this).parents('.card'),
      body = parent.children('.card-block');
    if (body.is(':visible')) {
      parent.addClass('card-collapsed');
      body.slideUp(200);
    } else if (!body.is(':visible')) {
      parent.removeClass('card-collapsed');
      body.slideDown(200);
    }
    e.preventDefault();
    e.stopPropagation();
  });

  /******** Card refresh control ********/
  $('[data-toggle=card-refresh]').on('click', function(e) {
    var parent = $(this).parents('.card');
    parent.addClass('card-refreshing');
    window.setTimeout(function() {
      parent.removeClass('card-refreshing');
    }, 3000);
    e.preventDefault();
    e.stopPropagation();
  });

  /******** Card remove control ********/
  $('[data-toggle=card-remove]').on('click', function(e) {
    var parent = $(this).parents('.card');
    parent.addClass('animated zoomOut');
    parent.bind('animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd', function() {
      parent.remove();
    });
    e.preventDefault();
    e.stopPropagation();
  });

  /******** Search form ********/
  $('.search-form .form-control').focusout(function() {
    $('.header-inner').removeClass('search-focus');
    searchState = false;
  }).focusin(function() {
    $('.header-inner').addClass('search-focus');
    searchState = true;
  });

  /******** Sidebar toggle menu ********/
  $('[data-toggle=sidebar]').on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    toggleMenu();
  });
  $('.main-panel').on('click', function(e) {
    var target = e.target;
    if (menuState && target !== $('[data-toggle=sidebar]') && !$('.header-secondary')) {
      toggleMenu();
    }
  });

  /******** Sidebar menu ********/
  $('.sidebar-panel nav a').on('click', function(e) {
    var $this = $(this),
      links = $this.parents('li'),
      parentLink = $this.closest('li'),
      otherLinks = $('.sidebar-panel nav li').not(links),
      subMenu = $this.next();
    if (!subMenu.hasClass('sub-menu')) {
      toggleMenu();
      return;
    }
    otherLinks.removeClass('open');
    if (subMenu.is('ul') && (subMenu.height() === 0)) {
      parentLink.addClass('open');
    } else if (subMenu.is('ul') && (subMenu.height() !== 0)) {
      parentLink.removeClass('open');
    }
    if (subMenu.is('ul')) {
      return;
    }
    e.stopPropagation();
    return;
  });
  $('.sidebar-panel').find('> li > .sub-menu').each(function() {
    if ($(this).find('ul.sub-menu').length > 0) {
      $(this).addClass('multi-level');
    }
  });

  /******** Demo only ********/
  function getURLParameter(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
  }

  var layout = getURLParameter('layout');

  if (layout) {
    switch(layout) {
      case "offcanvas":
        $('.app').addClass('offcanvas');
      break;
      case "expanding":
        $('.app').addClass('expanding');
      break;
      case "fixed":
        $('.app').addClass('fixed-header');
      break;
      case "boxed":
        $('.app').addClass('boxed');
      break;
      case "static":
        $('.app').addClass('static');
      break;
    }
  }

  $('<div class="configuration layout-column flex hidden-sm-down"> <div class="configuration-cog toggle-options"> <img src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDU0IDU0IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1NCA1NDsiIHhtbDpzcGFjZT0icHJlc2VydmUiIHdpZHRoPSI1MTJweCIgaGVpZ2h0PSI1MTJweCI+CjxnPgoJPHBhdGggc3R5bGU9ImZpbGw6I0M3Q0FDNzsiIGQ9Ik02LDBDNS40NDgsMCw1LDAuNDQ3LDUsMXY0MGMwLDAuNTUzLDAuNDQ4LDEsMSwxczEtMC40NDcsMS0xVjFDNywwLjQ0Nyw2LjU1MiwwLDYsMHoiLz4KCTxwYXRoIHN0eWxlPSJmaWxsOiNDN0NBQzc7IiBkPSJNNDgsMTJjLTAuNTUyLDAtMSwwLjQ0Ny0xLDF2NDBjMCwwLjU1MywwLjQ0OCwxLDEsMXMxLTAuNDQ3LDEtMVYxM0M0OSwxMi40NDcsNDguNTUyLDEyLDQ4LDEyeiIvPgoJPHBhdGggc3R5bGU9ImZpbGw6I0M3Q0FDNzsiIGQ9Ik0yNywwYy0wLjU1MiwwLTEsMC40NDctMSwxdjE5YzAsMC41NTMsMC40NDgsMSwxLDFzMS0wLjQ0NywxLTFWMUMyOCwwLjQ0NywyNy41NTIsMCwyNywweiIvPgoJPHBhdGggc3R5bGU9ImZpbGw6I0M3Q0FDNzsiIGQ9Ik0yNywzMmMtMC41NTIsMC0xLDAuNDQ3LTEsMXYyMGMwLDAuNTUzLDAuNDQ4LDEsMSwxczEtMC40NDcsMS0xVjMzQzI4LDMyLjQ0NywyNy41NTIsMzIsMjcsMzJ6Ii8+CjwvZz4KPGNpcmNsZSBzdHlsZT0iZmlsbDojNzM4M0JGOyIgY3g9IjYiIGN5PSI0NyIgcj0iNiIvPgo8Y2lyY2xlIHN0eWxlPSJmaWxsOiMyNkI5OUE7IiBjeD0iMjYuNzkzIiBjeT0iMjYuNzkzIiByPSI2LjIwNyIvPgo8Y2lyY2xlIHN0eWxlPSJmaWxsOiM3MzgzQkY7IiBjeD0iNDgiIGN5PSI3IiByPSI2Ii8+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo="/> </div> <div class="configuration-options flex scroll-y"> <div class="title"> Layouts </div> <div class="row text-xs-center options"> <div class="col-xs-6"> <a href="index.html"> <img src="images/layouts/default.png" class="img-fluid"> </a> <div class="m-b-2">Default</div> </div> <div class="col-xs-6"> <label> <input name="offcanvas" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/offcanvas.png" class="img-fluid"> </label> <div class="m-b-2">Offcanvas Sidebar</div> </div> <div class="col-xs-6"> <label> <input name="expanding" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/expanding.png" class="img-fluid"> </label> <div class="m-b-2">Expanding Sidebar</div> </div> <div class="col-xs-6"> <label> <input name="fixed-header" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/default.png" class="img-fluid"> </label> <div class="m-b-2">Fixed header</div> </div> <div class="col-xs-6"> <label> <input name="boxed" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/boxed.png" class="img-fluid"> </label> <div class="m-b-2">Boxed Wrapper</div> </div> <div class="col-xs-6"> <label> <input name="static" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/default.png" class="img-fluid"> </label> <div class="m-b-2">Static Sidebar</div> </div> <div class="col-xs-6"> <label> <input name="search-focus-active" type="checkbox"/> <i class="material-icons">check</i> <img src="images/layouts/default.png" class="img-fluid"> </label> <div class="m-b-2">Expanding Search</div> </div> <div class="col-xs-6"> <a href="index-horizontal.html"> <img src="images/layouts/horizontal.png" class="img-fluid"> </a> <div class="m-b-2">Horizontal Nav</div> </div> </div> <div class="option text-uppercase m-t-2"> Example Skins </div> <div class="row"> <div class="col-xs-6"> <div class="theme-options"> <label> <input name="theme-choice" type="radio" value="skin-default"> <i class="material-icons"> check </i> <div> <span> <span class="bg-white"> </span> <span class="bg-white"> </span> </span> <span class="bg-primary"> </span> </div> </input> </label> </div> </div> <div class="col-xs-6"> <div class="theme-options"> <label> <input name="theme-choice" type="radio" value="skin-1"> <i class="material-icons"> check </i> <div> <span> <span class="bg-white"> </span> <span class="bg-white"> </span> </span> <span class="bg-success"> </span> </div> </input> </label> </div> </div> <div class="col-xs-6"> <div class="theme-options"> <label> <input name="theme-choice" type="radio" value="skin-2"> <i class="material-icons"> check </i> <div> <span> <span class="bg-white"> </span> <span class="bg-white"> </span> </span> <span class="bg-info"> </span> </div> </input> </label> </div> </div> <div class="col-xs-6"> <div class="theme-options"> <label> <input name="theme-choice" type="radio" value="skin-3"> <i class="material-icons"> check </i> <div> <span> <span class="bg-white"> </span> <span class="bg-white"> </span> </span> <span class="bg-warning"> </span> </div> </input> </label> </div> </div> <div class="col-xs-6"> <div class="theme-options"> <label> <input name="theme-choice" type="radio" value="skin-4"> <i class="material-icons"> check </i> <div> <span> <span class="bg-dark"> </span> <span class="bg-dark"> </span> </span> <span class="bg-primary"> </span> </div> </input> </label> </div> </div> </div> </div> </div>').appendTo('body');
  $('.configuration').on('click', '.toggle-options', function (e){e.stopPropagation(); e.preventDefault(); $('.configuration').toggleClass('active'); });
  $('.configuration').on('change', 'input[type="checkbox"]', function (e) {var name = $(this).attr('name'); if (name !== 'search-focus-active') {if (name === 'offcanvas' && $(this).is(':checked') && $('.app').hasClass('expanding')) {$('.app').removeClass('expanding'); $('input[name="expanding"]').prop('checked' , false); } if (name === 'expanding' && $(this).is(':checked') && $('.app').hasClass('offcanvas')) {$('.app').removeClass('offcanvas'); $('input[name="offcanvas"]').prop('checked' , false); } if ($(this).is(':checked')) {$('.app').addClass(name); } else {$('.app').removeClass(name); } } else {if ($(this).is(':checked')) {$('.header-inner').addClass(name); } else {$('.header-inner').removeClass(name); } } $('.options label').removeClass('active'); if ($(this).is(':checked')) {$(this).parent().addClass('active');} }); $('.configuration').on('change', 'input[type="radio"]', function (e) {var value = $(this).val(); $('body').removeClass().addClass(value); });

})(jQuery);
