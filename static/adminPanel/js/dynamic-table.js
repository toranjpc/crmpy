var Script = function () {

    // begin first table
    $('#sample_1').dataTable({
        "ordering": false,
        "sDom": "<'row mb-4'<'col-sm-6 text-right'f><'col-sm-6'l>r>t<'row mt-4'<'col-sm-6 text-right'i><'col-sm-6'p>>",
        // "sPaginationType": "bootstrap",
        language: {
            url: '/elements/adminPanel/assets/DataTables/fa.json',
        },
        // "aoColumnDefs": [{
        //     'bSortable': false,
        //     'aTargets': [0]
        // }]
    });

    jQuery('#sample_1_wrapper .dataTables_filter input').addClass("form-control"); // modify table search input
    jQuery('#sample_1_wrapper .dataTables_length select').addClass("form-control"); // modify table per page dropdown

    // begin second table
    // $('#sample_2').dataTable({
    //     "sDom": "<'row'<'col-sm-6'l><'col-sm-6'f>r>t<'row'<'col-sm-6'i><'col-sm-6'p>>",
    //     "sPaginationType": "bootstrap",
    //     "oLanguage": {
    //         "sLengthMenu": "_MENU_ per page",
    //         "oPaginate": {
    //             "sPrevious": "Prev",
    //             "sNext": "Next"
    //         }
    //     },
    //     "aoColumnDefs": [{
    //         'bSortable': false,
    //         'aTargets': [0]
    //     }]
    // });
    // /*
    // jQuery('#sample_2 .group-checkable').change(function () {
    //     var set = jQuery(this).attr("data-set");
    //     var checked = jQuery(this).is(":checked");
    //     jQuery(set).each(function () {
    //         if (checked) {
    //             $(this).attr("checked", true);
    //         } else {
    //             $(this).attr("checked", false);
    //         }
    //     });
    //     jQuery.uniform.update(set);
    // });
    // */
    // jQuery('#sample_2_wrapper .dataTables_filter input').addClass("form-control"); // modify table search input
    // jQuery('#sample_2_wrapper .dataTables_length select').addClass("form-control"); // modify table per page dropdown

    // // begin: third table
    // $('#sample_3').dataTable({
    //     "sDom": "<'row'<'col-sm-6'l><'col-sm-6'f>r>t<'row'<'col-sm-6'i><'col-sm-6'p>>",
    //     "sPaginationType": "bootstrap",
    //     "oLanguage": {
    //         "sLengthMenu": "_MENU_ per page",
    //         "oPaginate": {
    //             "sPrevious": "Prev",
    //             "sNext": "Next"
    //         }
    //     },
    //     "aoColumnDefs": [{
    //         'bSortable': false,
    //         'aTargets': [0]
    //     }]
    // });
    // /*
    // jQuery('#sample_3 .group-checkable').change(function () {
    //     var set = jQuery(this).attr("data-set");
    //     var checked = jQuery(this).is(":checked");
    //     jQuery(set).each(function () {
    //         if (checked) {
    //             $(this).attr("checked", true);
    //         } else {
    //             $(this).attr("checked", false);
    //         }
    //     });
    //     jQuery.uniform.update(set);
    // });
    // */

    // jQuery('#sample_3_wrapper .dataTables_filter input').addClass("form-control"); // modify table search input
    // jQuery('#sample_3_wrapper .dataTables_length select').addClass("form-control"); // modify table per page dropdown



}();