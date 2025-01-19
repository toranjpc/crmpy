var $OptionsArr = {};
(function ($) {
   $.fn.customSelect = function (_options = {}, $OpenIt = 0, addtolist = '') {
      return this.each(function (val, i) {
         let __options = $.extend({}, {
            search: true,
            hover: false,
            responsive: true,
            checkboxes: true,
            scrollToSelect: true,
            closeAfterSelect: true,
            ajaxrequest: '',
            beforeRenderList: (item) => { },
            onSelect: (element, item) => { },
         }, _options)

         if (isMobile()) {
            __options.hover = false
            __options.closeAfterSelect = true
         }

         let select = $(this)
         let options = select.find('option')
         let selected = select.find('option:selected')

         // $(this).css('display', 'none');

         if (select.next().hasClass('selectPlug')) {
            select.next('.selectPlug').remove()
         }

         let _htmlTemplate = `
            <div id="${select.attr('name')}" class="selectPlug baseselectdiv" name="${select.attr('name')}">
               <li class="down ${__options.hover ? 'hover' : ''}">
                  <span class="selectPlug-label">${select.find('option:first').text()}</span>
                  <ul class="selectPlug-menu p-0">
                     <div class="selectPlug-search">
                        <div class="selectPlug-inline">
                              <span class="selectPlug-close">×</span>
                        </div>
                        <input type="text" name="selectPlug-search" class="form-control ${select.hasClass('justajax') ? 'justajax' : ''}" placeholder="Search" />
                     </div>
                     <ul class="selectPlug-list" /></ul>
                  </ul>
                  <div class="overlay" />
               </li>
            </div>
         `;

         select.after(_htmlTemplate)

         let $select = select.next()
         let $label = $select.find('.selectPlug-label')
         let $menu = $select.find('.selectPlug-menu')
         let $list = $select.find('.selectPlug-list')

         let $searchContainer = $select.find('.selectPlug-search')
         let $search = $menu.find('[name=selectPlug-search]')
         $search.attr("data-url", __options.ajaxrequest);
         if (__options.search) {
            $search.on('keypress', (e) => {
               // e.preventDefault();
               var key = e.which || e.keyCode || 0;
               if (key == 13) {
                  let find = $(e.currentTarget).val().toLowerCase()
                  if (__options.ajaxrequest != '' && $(this).hasClass("justajax") && find.length > 2) {
                     $list.html(`<li class="text-center loadli"><div class="row d-flex justify-content-center"><img src="/flatlab/img/Loader.gif" class="w-50" /><p class="col-12" dir="rtl">درحال بارگزاری ...</p></div></li>`);
                     let url = __options.ajaxrequest;
                     $.ajax({
                        headers: {
                           'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                        },
                        type: "POST",
                        data: { 'title': find, 'paginate': 4 },
                        url: url,
                        cache: false,
                        error: function (data) {
                           $("#loading").addClass('d-none');
                        },
                        success: function (data, textStatus, jqXHR) {
                           $list.html('');
                           select.html('');
                           data.Data.forEach((element) => {
                              select.append(`<option value="${element.id}">${element.key}</option>`);
                           });
                           let addtolist = '';
                           if (data.TotalPage > data.CurrentPage) addtolist = `<div class="row d-flex justify-content-center btn btn-secondary loadmore" style="position: sticky;"><p class="m-0">نمایش بیشتر</p></div>`;
                           select.customSelect(__options, find, addtolist);
                        }
                     });
                  }
                  return false;
               }
            })
            $search.on('keyup', (e) => {
               let find = $(e.currentTarget).val().toLowerCase()
               $list.find('li').not(".loadli").each((i, element) => {
                  let value = $(element).text().toLowerCase()
                  if (value.indexOf(find) == -1) {
                     $(element).hide()
                  } else {
                     $(element).show()
                  }
               })
            });
         }
         options.each((i, element) => {
            let opt = $(element)
            let img = $(element).attr('data-img') || '';
            if (!opt.attr('value')) {
               $searchContainer.find('.selectPlug-inline').prepend(`
                  <span class="select-title">${opt.text()}</p></span>
               `)
               return
            }

            let listItem = `<li 
               ${!opt.attr('data-img') ? '' : `data-img="${opt.attr('data-img')}"`}
               ${!opt.attr('title') ? '' : `title="${opt.text()}"`}
               ${!opt.attr('value') ? '' : `data-value="${opt.val()}"`}
               ${!opt.is(':selected') && !opt.is(':disabled') ? '' : `class="${opt.is(':selected') ? 'selected' : 'disabled'}"`}
            />${__options.checkboxes ? `<span><p>${opt.text()}</p></span>` : opt.text()}`

            if (__options.beforeRenderList && typeof __options.beforeRenderList === 'function' && __options.beforeRenderList.toString().includes('return')) {
               if (opt.prop('value').length) {
                  let res = __options.beforeRenderList.call(this, {
                     id: opt.index(),
                     value: opt.val(),
                     text: opt.text(),
                     img: opt.attr('data-img'),
                  })

                  listItem = `<li 
                        ${!opt.attr('title') ? '' : `title="${opt.text()}"`}
                        ${!opt.attr('value') ? '' : `data-value="${opt.val()}"`}
                        ${!opt.is(':selected') && !opt.is(':disabled') ? '' : `class="${opt.is(':selected') ? 'selected' : 'disabled'}"`}
                     >${__options.checkboxes ? `<span><p>${res}</p></span>` : res}</li>`
               }
            }

            $list.append(listItem)
         })
         $list.find('li').each((i, element) => {
            $(element).bind('click', (e) => {
               let current = $(e.currentTarget)

               if (current.hasClass('disabled'))
                  return

               if (current.hasClass('selected')) {
                  current.removeClass('selected')
                  let firstOption = options.first()
                  firstOption.prop('selected', true)
                  $label.text(selected.text())
                  return
               }

               $list.find('li').removeClass('selected');
               current.addClass('selected');

               $label.text(current.text())
               select.val(!current.data('value') ? current.text() : current.data('value'))

               if (typeof __options.onSelect === 'function') {
                  $($select).find("option[value='" + current.data('value') + "']").prop("selected", true);
                  return __options.onSelect.call(this, $select, {
                     id: current.index(),
                     value: current.data('value'),
                     text: current.text()
                  })
               }
            })
         })

         $label.on(__options.hover ? 'mouseover' : 'click', (e) => {
            let parent = $(e.currentTarget).parent();

            if (__options.hover) {
               parent.addClass('hover')
            } else {
               parent.toggleClass('visible')
            }
            if (__options.scrollToSelect) {
               let scrollTo = parent.find('.selected');
               if (scrollTo.length > 0) {
                  $menu.scrollTop(parent.find('.selected').get(0).offsetTop)
               }
            }
            if (isMobile()) {
               if (__options.responsive) {
                  $menu.addClass('responsive')
                  $('body').addClass('select-overflow-hidden')
               } else {
                  $('body').removeClass('select-overflow-hidden')
               }
            } else {
               selectPositionFix()
               $menu.removeClass('responsive')
            }
            if (!__options.search) {
               $searchContainer.remove()
            }
            let firstListEntry = $list.find('li:first');
            if (firstListEntry.text() == options.first().text()) {
               firstListEntry.hide()
            }
         })

         $(document).mouseup((e) => {
            if (!$menu.is(':visible')) {
               e.preventDefault()
            }
            let selectMenu = $menu
            if (!__options.hover) {
               if (__options.closeAfterSelect) {
                  if ((!selectMenu.is(e.target) &&
                     $(e.target).attr('name') !== 'selectPlug-search' &&
                     $(e.target).attr('class') !== 'select-list' &&
                     $(e.target).attr('class') !== 'select-title' &&
                     !$(e.target).hasClass('disabled') &&
                     $(e.target).hasClass('loadmore') &&
                     !$(e.target).hasClass('selected')
                  )) {
                     $('body').removeClass('select-overflow-hidden')
                     $select.find('li:first').removeClass('visible');
                     $search.val('').trigger('keyup')
                  }
               } else {
                  if ((!selectMenu.is(e.target) &&
                     $(e.target).attr('name') !== 'selectPlug-search' &&
                     $(e.target).attr('class') !== 'select-list' &&
                     $(e.target).attr('class') !== 'select-title' &&
                     $(e.target).prop('tagName') !== 'LI' &&
                     $(e.target).prop('tagName') !== 'P' &&
                     $(e.target).prop('tagName') !== 'SPAN' &&
                     !$(e.target).hasClass('disabled') &&
                     !$(e.target).hasClass('selected') ||
                     $(e.target).hasClass('loadmore') &&
                     $(e.target).hasClass('select-close')
                  )) {
                     $('body').removeClass('select-overflow-hidden')
                     $select.find('li:first').removeClass('visible');
                     $search.val('').trigger('keyup')
                  }
               }
            } else {
               if (__options.closeAfterSelect) {
                  $('body').removeClass('select-overflow-hidden')
                  selectMenu.parent().removeClass('hover')
                  $select.find('li:first').removeClass('visible');
               }
               $search.val('').trigger('keyup')
            }
            if ($label.text() != selected.text()) {
               $label.text(select.find('option:selected').text())
            }
         })

         select.on('change', () => {
            let value = $(this).val()
            $list.find('li').each((i, element) => {
               if (value == $(element).data('value')) {
                  $(element).click()
               }
            })
         })
         select.on('deselect', () => {
            $list.find('li:first').click()
         })
         select.on('select', (e, newValue) => {
            $(this).val(newValue)
            $list.find('li').each((i, element) => {
               if (newValue == $(element).data('value')) {
                  if (!$(element).hasClass('selected')) $(element).click()
               }
            })
         })
         select.on('destroy', () => {
            if ($(this).next().hasClass('selectPlug'))
               $(this).next('.selectPlug').remove();
         })
         select.on('rebuild', (e, o) => {
            if (!$(this).next().length) {
               if (!o) o = __options
               $(this).customSelect(o);
            }
         })
         select.on('close', (e, o) => {
            if ($menu.is(':visible')) {
               $label.click()
            }
         })
         select.on('open', (scrollIntoView) => {
            if ($menu.is(':hidden')) {
               $label.click()
               if (scrollIntoView && !isMobile()) {
                  $select.get(0).scrollIntoView({
                     behavior: 'smooth',
                     block: 'nearest'
                  });
               }
            }
         })
         $(window).on('resize scroll', selectPositionFix)

         function isMobile() {
            return window.matchMedia(`(max-width: 600px)`).matches
         }

         function selectPositionFix() {
            let watch = $select
            let offset = 25

            let elementTop = watch.offset().top
            let windowHeight = $(window).height()
            let elementBottom = elementTop + watch.outerHeight() + offset
            let viewportTop = $(window).scrollTop() - offset
            let viewportBottom = viewportTop + windowHeight

            let isInViewport = elementBottom > viewportTop && elementTop < viewportBottom
            let menuBottom = elementTop < viewportBottom - $menu.outerHeight()
            let menuTop = elementTop > viewportBottom - $menu.outerHeight()

            if (windowHeight < 500) {
               $searchContainer.css('position', 'static')
            } else {
               $searchContainer.css('position', 'sticky')
            }

            if (isInViewport) {
               let elem = $select.find('li:first')
               if (menuBottom) {
                  elem.removeClass('up').addClass('down')
               }
               if (menuTop) {
                  $select.find('li:first').removeClass('down').addClass('up')
               }
            } else {
               if ($menu.is(':visible')) {
                  select.trigger('close')
               }
            }
            if (isMobile()) {
               if (__options.responsive) {
                  $menu.addClass('responsive')
               }
            }
         }

         if ($OpenIt) {
            $label.click();
            $search.val($OpenIt);
         }
         if (addtolist != '') {
            $list.after(addtolist);
         }

         $OptionsArr[select.attr('name')] = __options;
         // console.log($OptionsArr[select.attr('name')]);

      })
   }

}(jQuery));

var $pagenumber = [];
$(document).on('click', '.loadmore0', function (e) {
   let parent = $(this).closest('div.baseselectdiv')
   let optioid = parent.attr('id')
   let $q = $pagenumber[optioid] || 2;
   let find = parent.find("[name='selectPlug-search']").val()
   if (find.length > 2) {
      let $url = $(parent).find("[name='selectPlug-search']").attr('data-url');
      let $list = $(parent).find('ul.selectPlug-list');
      let select = $(parent).prev('select')

      $list.html(`<li class="text-center loadli"><div class="row d-flex justify-content-center"><img src="/flatlab/img/Loader.gif" class="w-50" /><p class="col-12" dir="rtl">درحال بارگزاری ...</p></div></li>`);
      $.ajax({
         headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
         },
         type: "POST",
         data: { 'title': find, 'paginate': 4 },
         url: $url + '?q=' + $q,
         cache: false,
         error: function (data) {
            $("#loading").addClass('d-none');
         },
         success: function (data, textStatus, jqXHR) {
            data.Data.forEach((element) => {
               select.append(`<option value="${element.id}">${element.key}</option>`);
            });
            let addtolist = '';
            if (data.TotalPage > data.CurrentPage) addtolist = `<div class="row d-flex justify-content-center btn btn-secondary loadmore" style="position: sticky;"><p class="m-0">نمایش بیشتر</p></div>`;
            $pagenumber[optioid] = data.CurrentPage * 1 + 1;
            select.customSelect(categoryoptions, find, addtolist);//$OptionsArr[optioid]
            alert($pagenumber);
         }
      });
   }
});


   /*
    let options = {
        search: true,
        hover: false,
        responsive: true,
        checkboxes: true,
        scrollToSelect: true,
        closeAfterSelect: true,
        ajaxrequest: '',
        beforeRenderList: (item) => {
            // // console.log(item);
            var $X = '';
            if (item.img) $X = `<img src="${item.img.toLowerCase()}" width="20" />`;
            return $X + ' ' + item.text.toLowerCase();
        },
        onSelect: (element, item) => {
            // $(element).remove();
            // // console.log(element, item)
            // // console.log(item)
        },
    }
    let categoryoptions = {
        search: true,
        hover: false,
        responsive: true,
        checkboxes: true,
        scrollToSelect: true,
        closeAfterSelect: true,
        ajaxrequest: "{{route('usercategoryapi')}}",
        beforeRenderList: (item) => {
            // // console.log(item);
            var $X = '';
            if (item.img) $X = `<img src="${item.img.toLowerCase()}" width="20" />`;
            return $X + ' ' + item.text.toLowerCase();
        },
        onSelect: (element, item) => {
            // $(element).remove();
            // // console.log(element, item)
            // // console.log(item)
        },
    }
    $(document).ready(function() {
        $('select').not("select[name='category']").customSelect(options);
        $("select[name='category']").customSelect(categoryoptions);
    });
    */
