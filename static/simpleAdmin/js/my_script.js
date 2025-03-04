

/******** start my script */

$(document).keyup(function (e) {
    var key = e.which || e.keyCode || 0;
    // // console.log(key);
    if (key == 27) $("#magiceMenu").prop("hidden", true).next("#magiceMenuShadow").prop("hidden", true);
    if (e.ctrlKey && key == 32) {
        e.preventDefault();
        // $("input#elements_search").val("").focus();
        $("#magiceMenu").removeAttr("hidden").find("#SearchMenu").select2('open');//.select2('focus');
        $("#magiceMenuShadow").removeAttr("hidden");//.select2('focus');
    }
});
// $(document).keydown(function (e) {
//     // e.preventDefault();
//     var key = e.which || e.keyCode || 0;
//     // alert(key);
//     CtrlKey = false;
//     EscKey = false;
//     if (e.CtrlKey) CtrlKey = true;
//     if (e.shiftKey) shiftKey = true;
//     if (key == 27) EscKey = true;
// });
$(document).on("mouseover", "td , th", function () {
    $(".table_hidden_hover").addClass("d-none");
    $(this).closest("tr").find(".table_hidden_hover").removeClass("d-none");
    $(this).closest("th").find(".table_hidden_hover").removeClass("d-none");
});
$(document).on("mouseover", ".hidden_div", function () {
    $(".hidden_element").addClass("d-none");
    $(this).find(".hidden_element").removeClass("d-none");
});

function moneyformat(number) {
    var decimalSeparator = ".";
    var thousandSeparator = ",";
    var result = String(number);
    var parts = result.split(decimalSeparator);
    result = parts[0].split("").reverse().join("");
    result = result.replace(/(\d{3}(?!$))/g, "$1" + thousandSeparator);
    parts[0] = result.split("").reverse().join("");
    return parts.join(decimalSeparator);
}

function SZ(val) {
    var separator = ",";
    var int = val.value.replace(new RegExp(separator, "g"), "");
    var regexp = new RegExp("\\B(\\d{3})(" + separator + "|$)");
    do {
        int = int.replace(regexp, separator + "$1");
    }
    while (int.search(regexp) >= 0)
    val.value = int;
}
$(document).on("blur", ".money", function () {
    if (!$(this).val().trim()) $(this).val(0);
});
$(document).on("keyup", ".money", function () {
    SZ(this);
});
$(document).on('keypress', '.only_number', function (e) {
    if (e.which != 13 && e.which != 45 && e.which != 46 && (e.which < 48 || e.which > 57)) {
        // alert(e.which);
        return false;
    }
});
$(document).on('click', '[data-request]', function (e) {
    e.preventDefault();
    var thiss = $(this);
    var nRow = $(this).closest('tr').attr("id");
    var $url = $(this).attr('data-request');
    var content = $(this).attr("data-content") ? $(this).attr("data-content") : 'از حذف این مورد اطمینان دارید ؟';
    // var content = typeof CONF_CONTENT !== 'undefined' ? CONF_CONTENT : 'از حذف این مورد اطمینان دارید ؟';
    var dofunc = (data, vales) => {
        location.reload();
    };
    if (typeof dofuncinline !== 'undefined') {
        var dofunc = dofuncinline;
        dofuncinline = undefined;
    }
    $.confirm({
        title: 'توجه !!!',
        content: content,
        type: 'red',
        columnClass: 'small',
        backgroundDismiss: true,
        backgroundDismissAnimation: 'glow',
        theme: 'Modern',
        // icon: 'icon-trash',
        animation: 'scale',
        autoClose: 'cancel|4000',
        buttons: {
            ok: {
                text: 'ادامه',
                btnClass: 'btn-danger',
                keys: ['enter'],
                action: function () {
                    var self = this;
                    ajaxRequest($url, null, dofunc, noalert = 0);
                }
            },
            cancel: {
                text: 'انصراف',
                keys: ['esc'],
                action: function () { }
            }
        }
    });
    return false;
});

function showforms(formData) {
    let formRenderOpts = {
        dataType: 'json',
        formData
    };
    let $renderContainer = $('<div/>');
    $renderContainer.formRender(formRenderOpts);
    return $renderContainer.html();
}

function set_form_val(vals) {
    jQuery.each(vals, function (input_name, input_val) {
        var tis_input = $(document).find("[name='" + input_name + "']");
        if ($(tis_input).is("select")) {
            $(tis_input).find("option").prop("selected", false);
            if (Array.isArray(input_val)) {
                for (let c = 0; c < input_val.length; c++) {
                    $(tis_input).find("option[value='" + input_val[c] + "']").prop("selected", true);
                }
            } else {
                $(tis_input).find("option[value='" + input_val + "']").prop("selected", true);
            }
        } else if ($(tis_input).attr("type") == 'radio') {
            $(tis_input).prop('checked', false);
            $(document).find("[name='" + input_name + "'][value='" + input_val + "']").prop('checked', true).change();
        } else if ($(tis_input).attr("type") == 'checkbox') {
            $(tis_input).prop('checked', false);
            if (Array.isArray(input_val)) {
                for (let c = 0; c < input_val.length; c++) {
                    $(document).find("[name='" + input_name + "'][value='" + input_val[c] + "']").prop('checked', true);
                }
            } else {
                $(document).find("[name='" + input_name + "'][value='" + input_val + "']").prop('checked', true);
            }
        } else if ($(tis_input).attr("type") == 'file') {
            if (Array.isArray(input_val)) {
                $DD = '';
                for (let Z = 0; Z < input_val.length; Z++) {
                    $DD += '<tr><td>' + parseInt(Z + 1) + '</td><td><input class="file_input" type="hidden" name="' + input_name + '[]" value="' + input_val[Z] + '"><a href="/' + input_val[Z] + '" target="_blank">' + input_val[Z] + '</a></td></tr>';
                }
                $(tis_input).after('<table class="table table-hover filessss"><tbody>' + $DD + '</tbody></table>');
            } else {
                $(tis_input).after('<table class="table table-striped table-hover"><tbody><tr><td><input class="file_input" type="hidden" name="' + input_name + '[]" value="' + input_val + '"><a href="/' + input_val + '" target="_blank">' + input_val + '</a></td></tr></tbody></table>');
            }
        } else if (($(tis_input).is("input") && !$(tis_input).hasClass("file_input")) || $(tis_input).is("textarea")) {
            $(tis_input).val(input_val);
        }
    });
}

$('#show_form').click(function () {
    $("#add_panel").toggleClass('d-none');
    $("#edit_panel").addClass('d-none');

    $(".catidlist").addClass("d-none");
    $(".viwe_opti").addClass("d-none");
    $(".chang_cat").removeClass("d-none");
});
function copyToClipboard(text) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}

$(document).on("click", ".share_it", function (event) {
    var title = $(this).attr("title");
    var url = $(this).attr("link");
    if (navigator.share) {
        navigator
            .share({
                title,
                url
            })
            .then(() => {
                copyToClipboard(url);
            })
            .catch(console.error);
    } else {
        copyToClipboard(url);
    }
});

$(document).on("click", ".gallery", function () {
    $('#gallery_modal').find('.modal-content').html(`<img class="" style="width:unset" src="${$(this).attr('src')}" />`);
    $('#gallery_modal').modal('show');
});

var SetProvinces = (address = [0, 0]) => {
    let provinces = [];
    $.getJSON("/assets/provinces/states.php", {
        acc: true
    }, function (data) {
        provinces = data.entries;
        let citi_id = 0;
        for (let i = 0; i < provinces.length; i++) {
            if (provinces[i].title == address[0]) citi_id = i;
            $("select.provinces").append('<option data-value="' + provinces[i].code + '" data-provinces="' + i + '">' + provinces[i].title + '</option>');
        }
        $(document).find(`select.provinces option[data-value='${address[6]}']`).prop("selected", true).change();
        $(document).find(`select.cities option[data-value='${address[7]}']`).prop("selected", true);

        $("input#active_state").val(address[6]);
        $("input#active_citie").val(address[7]);

    });
    $(document).on("change", "select.provinces", function () {
        $("select.cities").html('<option data-provinces="Z" value="" hidden>انتخاب شهر</option>');
        var citi_cod = $(this).find("option:selected").attr("data-provinces");
        if (citi_cod == 'z' || !provinces[citi_cod]) return false;
        const cities = provinces[citi_cod].cities;
        for (let i = 0; i < cities.length; i++) {
            $("select.cities").append('<option data-value="' + cities[i].code + '">' + cities[i].title + '</option>');
        }
        $("#active_state").val($(this).find("option:selected").attr("data-value"));
        $("#active_citie").val("");
    });
    $(document).on("change", "select.cities", function () {
        $("#active_citie").val($(this).find("option:selected").attr("data-value"));
    });
}

(function ($) {
    $.fn.set_file = function (type, options) {
        type = type || 'elements';
        this.on('click', function (e) {
            var route_prefix = (options && options.prefix) ? options.prefix : '/filemanager';
            var target_input = $(this);
            window.open(route_prefix + '?type=' + type, 'FileManager', 'width=900,height=600');
            window.SetUrl = function (items) {
                var file_path = items.map(function (item) {
                    return item.url;
                }).join(',');
                // set the value of the desired input to image url
                target_input.val('').val(file_path).trigger('change');
            };
            return false;
        });
    }
})(jQuery);

function p_imageSet(input, imgs) {
    $(input).val("");
    var x_thumbs = [];
    var x_base = [];
    $(imgs).each(function (i) {
        var val = $(this).attr("src");
        var url = $(this).attr("data-url") || val.replace("thumbs/", "");
        x_thumbs.push(val);
        x_base.push(url);
    });
    var X = {
        'thumbs': x_thumbs,
        'base': x_base
    };
    $(input).val(JSON.stringify(X));
}

File.prototype.convertToBase64 = function (callback) {
    var reader = new FileReader();
    reader.onloadend = function (e) {
        callback(e.target.result, e.target.error);
    };
    reader.readAsDataURL(this);
};

function DataURIToBlob(dataURI) {
    const splitDataURI = dataURI.split(',')
    const byteString = splitDataURI[0].indexOf('base64') >= 0 ? atob(splitDataURI[1]) : decodeURI(splitDataURI[1])
    const mimeString = splitDataURI[0].split(':')[1].split(';')[0]

    const ia = new Uint8Array(byteString.length)
    for (let i = 0; i < byteString.length; i++)
        ia[i] = byteString.charCodeAt(i)

    return new Blob([ia], {
        type: mimeString
    })
}

$(document).on("keyup", "[min] , [max]", function () {
    var val = $(this).val() * 1 || 0;
    if (val > $(this).attr("max")) $(this).val(12);
    if (val < $(this).attr("min")) $(this).val(1);
});

// send ajax request
function ajaxRequest($url, $vales, $func, noalert = 0, methode = "POST") {
    $("#loading").removeClass('d-none');
    $.ajax({
        headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        type: methode,
        data: $vales,
        url: $url,
        cache: false,
        contentType: false,
        processData: false,
        statusCode: {
            200: function (data) {
                // // console.log(data);
                $("#loading").addClass('d-none');
                if (noalert == 1) return $func(data, $vales);
                $.confirm({
                    title: data.response,
                    content: false,
                    type: 'green',
                    columnClass: 'small',
                    backgroundDismiss: true,
                    backgroundDismissAnimation: 'glow',
                    theme: 'Modern',
                    icon: 'fa fa-check',
                    animation: 'scale',
                    autoClose: 'cancel|3000',
                    buttons: {
                        cancel: {
                            btnClass: 'd-none',
                            keys: ['esc', 'enter'],
                            action: function () { }
                        }
                    }
                });
                $func(data, $vales);
            },
            400: function (data) {
                $("#loading").addClass('d-none');
                if (noalert == 1) return $func(data, $vales);
                $.confirm({
                    title: 'خطا !!!',
                    content: data.responseJSON.response,
                    type: 'red',
                    columnClass: 'small',
                    backgroundDismiss: true,
                    backgroundDismissAnimation: 'glow',
                    theme: 'Modern',
                    icon: 'fa fa-times',
                    animation: 'scale',
                    autoClose: 'cancel|3000',
                    buttons: {
                        cancel: {
                            btnClass: 'd-none',
                            keys: ['esc', 'enter'],
                            action: function () { }
                        }
                    }
                });
            },
            422: function (data) {
                $("#loading").addClass('d-none');
                if (noalert == 1) return $func(data, $vales);
                data.responseJSON.errors.forEach((element, i) => {

                    $('body').prepend(`<div dir="rtl" class="alert text-dark alert-danger alert-dismissible show text-center mb-3" role="alert" data-dismiss="alert">${element}</div>`);

                    // var unique_id = $.gritter.add({
                    //     // (string | mandatory) the heading of the notification
                    //     title: data.responseJSON.response,
                    //     // (string | mandatory) the text inside the notification
                    //     text: element,
                    //     // (string | optional) the image to display on the left
                    //     image: false,
                    //     // (bool | optional) if you want it to fade out on its own or just sit there
                    //     sticky: true,
                    //     // (int | optional) the time you want it to be alive for before fading out
                    //     time: i * 1000,
                    //     // (string | optional) the class name you want to apply to that specific message
                    //     class_name: 'my-sticky-class text-right bg-danger'
                    // });
                });
            },
            500: function (data) {
                $("#loading").addClass('d-none');
                if (noalert == 1) return $func(data, $vales);
                $.confirm({
                    title: 'خطا !!!',
                    content: 'لطفا با پشتیبانی تماس بگیرید',
                    type: 'red',
                    columnClass: 'small',
                    backgroundDismiss: true,
                    backgroundDismissAnimation: 'glow',
                    theme: 'Modern',
                    icon: 'fa fa-times',
                    animation: 'scale',
                    autoClose: 'cancel|3000',
                    buttons: {
                        cancel: {
                            btnClass: 'd-none',
                            keys: ['esc', 'enter'],
                            action: function () { }
                        }
                    }
                });
            },
        },
        error: function (data) {
            // console.log(data);
            // location.reload();
        },
        success: function (data, textStatus, jqXHR) {
            // console.log(data);
            // // console.log([data, textStatus + ": " + jqXHR.status]);
            // $("#loading").addClass('d-none');
        }
    });
}
$('[required]').parent().addClass('requiredDiv');

$(document).on("click", "#toggleFullscreen", function () {

});


$("select[name='productId']").change(function () {
    // $(".BaseGaller").find("li.lslide.active").removeClass("active");
    // $(document).find(".previmage").remove();

    // let img = JSON.parse($(this).find("option:selected").attr("data-img"));

    // if (img) {
    //     let cloned_ = $(document).find(".BaseGaller ul li.lslide:first-child").clone();
    //     cloned_.addClass("active previmage");
    //     cloned_.find(".lslide img").attr("src", img.thumbs);
    //     $(document).find(".BaseGaller ul li.lslide:first-child").after(cloned_);
    // }


    let price = JSON.parse($(this).find("option:selected").attr("data-price"));
    $(".priceDiv").html(`
        ${(price[1] && price[1] != 'null' && price[1] != '0') ? '<del class="text-danger">' + moneyformat(price[1]) + '</del>' : ''}
        <span>${moneyformat(price[0])}</span>
    `);
});


var addToFavorit = (id, dis) => {
    // console.log($(dis).attr('class'));
    let Favorit = localStorage.getItem("Favorit") || '[]';
    Favorit = JSON.parse(Favorit);
    Favorit = Object.values(Favorit);

    const index = Favorit.indexOf(id);
    if (index > -1) {
        Favorit.splice(index, 1);
        $(dis).find(".fa-heart").removeClass("fa text-danger");
        if ($(dis).attr("data-placeholder")) {
            let tex = $(dis).find(".placeholder").text();
            $(dis).find(".placeholder").remove();
            $(dis).find("span:not(.placeholder)").text(tex);
        }
    } else {
        Favorit.push(id);
        $(dis).find(".fa-heart").addClass("fa text-danger");
        if ($(dis).attr("data-placeholder")) {
            $(dis).append(`<span class="placeholder d-none">${$(dis).text().trim()}</span>`);
            $(dis).find("span:not(.placeholder)").text($(dis).attr("data-placeholder"));
        }
    }
    let Favorit_ = [...new Set(Favorit)];
    Favorit_ = JSON.stringify(Favorit_);
    localStorage.setItem("Favorit", Favorit_);
}
// localStorage.clear();
$(document).ready(function () {
    /*
    let Favorit = localStorage.getItem("Favorit");
    Favorit = JSON.parse(Favorit);
    Favorit.forEach(element => {
        let dis = $(document).find(`[onclick^="addToFavorit('${element}'"]`);
        $(dis).find(".fa-heart").addClass("fa text-danger");
        if ($(dis).attr("data-placeholder")) {
            $(dis).append(`<span class="placeholder d-none">${$(dis).text().trim()}</span>`);
            $(dis).find("span:not(.placeholder)").text($(dis).attr("data-placeholder"));
        }
    });
    */
});

jQuery('input[type=checkbox].group-checkable').change(function () {
    if (jQuery(this).is(":checked")) {
        // $(".removeSelected").removeClass("d-none");
        jQuery(this).closest("table").find("tbody tr td:first-child").find("input[type=checkbox]").each(function () {
            $(this).prop("checked", true);
        });
        jQuery(this).closest("table").find("tbody tr td:first-child").find("input[type=checkbox]").change();

    } else {
        // $(".removeSelected").addClass("d-none");
        jQuery(this).closest("table").find("tbody tr td:first-child").find("input[type=checkbox]").each(function () {
            $(this).prop("checked", false);
        });
        jQuery(this).closest("table").find("tbody tr td:first-child").find("input[type=checkbox]").change();

    }
    // jQuery.uniform.update(set);
});

jQuery("table").find("tbody tr td:first-child").find("input[type=checkbox]").change(function () {
    var count = jQuery(this).closest("table").find("tbody tr td:first-child").find("input[type=checkbox]:checked").length;
    if (count > 0) {
        $(".removeSelected").removeClass("d-none");
    } else {
        $(".removeSelected").addClass("d-none");
    }
});

$(document).on("click", '[data-toggle="collapse"]', function (event) {
    id = $(this).attr("data-collapse");
    elenet = $(this).next(`[collapse-id='${id}']`);
    if (!elenet.length) return
    event.preventDefault();
    $(".collapse.show").slideUp(400, function () {
        $(".collapse.show").removeClass('show');
    });

    if ($(elenet).hasClass('show')) {
        $(elenet).slideUp(400, function () {
            $(elenet).removeClass('show');
        });
    } else {
        $(elenet).slideDown(400, function () {
            $(elenet).addClass('show');
        });
    }
});


/******** end my script */
