$(document).ready(function() {
    var $navIcon = $('#nav-icon2')
    var menu = $('.left-menu').sliiide({place: 'left', exit_selector: '.left-exit', toggle: '#nav-icon2'});
    var notes = $('.note');
    var toggles = $('.slider-toggle')
    var clickHandler = function() {
      var $button = $(this);
      if ($button.hasClass('selected')) {return;}
      $navIcon.removeClass('flip animated');
      notes.fadeOut(700);
      var place = $button.attr('data-link').split('-')[0];
      var menuPlace = $button.attr('data-link');
      var note;
      menu.reset();
      $button.addClass('selected');
      $('.slider-toggle').not($button).removeClass('selected');
      menu = $('.'+menuPlace).sliiide({place: place, exit_selector: '.'+place+'-exit', toggle: '#nav-icon2'});
      $navIcon.addClass('flip');
      $('.note[data-link="'+menuPlace+'"]').fadeIn(700).css('display','').removeClass('display-off');
    }
    toggles.on('click', clickHandler)
    } );
    
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');