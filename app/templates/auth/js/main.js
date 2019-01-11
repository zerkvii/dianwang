(function ($) {
    "use strict";


    /*==================================================================
   [ Focus input ]*/
    $('.input100').each(function () {
        $(this).on('blur', function () {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    })


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    // $('.validate-form').on('submit', function () {
    //     var check = true;
    //
    //     for (var i = 0; i < input.length; i++) {
    //         if (validate(input[i]) == false) {
    //             showValidate(input[i]);
    //             check = false;
    //         }
    //     }
    //
    //     return check;
    // });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    function getFormData($form) {
        let unindexed_array = $form.serializeArray();
        let indexed_array = {};
        $.map(unindexed_array, function (n) {
            indexed_array[n['name']] = n['value'];
        });
        return indexed_array;
    }

    function checkFormData() {
        let check = true;
        for (let i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }
        return check;
    }


    $("#register_btn").click(
        function (e) {
            e.preventDefault();

            if (checkFormData()) {
                $.ajax({
                    type: 'POST',
                    contentType: "application/json",
                    dataType: 'json',
                    url: window.location.search,
                    data: JSON.stringify(getFormData($('#register_form'))),
                    beforeSend: checkFormData(),
                    success: function (data) {
                        window.location.href = data['next_page'];
                    },
                    error: function (xhr) {
                        let information = $.parseJSON(xhr.responseText);
                        swal({
                            title: "错误",
                            text: information['information'],
                            icon: "error",
                            button: "确定"
                        },)
                    }
                })
            }
        }
    );

})(jQuery);
