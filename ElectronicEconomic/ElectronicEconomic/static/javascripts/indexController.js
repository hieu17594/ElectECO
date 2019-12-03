$(document).ready(function () {
    // $.ajax({
    //     type: "GET",
    //     url: "/api/contact",
    //     success: function (data) {
    //         $("#contactPhoneNumber").text(data.PhoneNumber);
    //         $("#contactEmail").text(data.Email);
    //     }
    // });
    //
    // $.ajax({
    //     type: "GET",
    //     url: "/api/languages",
    //     success: function (data) {
    //         $("#contactPhoneNumber").text(data.PhoneNumber);
    //         $("#contactEmail").text(data.Email);
    //     }
    // });

    $.ajax({
        type: "GET",
        url: "/api/categories",
        success: function (data) {
            if (data != null) {
                data.forEach((cate, index) => {
                    var subCategory = $("<ul>");

                    cate.sub_category.forEach(subcate => {
                        subCategory.append($("<li>").append($("<a>", {"href": "#"}).text(subcate.category)))
                    });
                    var x = 1;
                    $("#accordian").append($("<div>").addClass("panel panel-default").append(
                        $("<div>").addClass("panel-heading").append(
                            $("<a>").attr({
                                'data-toggle' : 'collapse',
                                'data-parent' : "#accordian",
                                'href' : "#item" + index
                            }).text(cate.category).append(
                                $("<span>", {"class": "badge pull-right"}).append($("<i>",{"class": "fa fa-plus"}))
                            )
                        ),
                        $("<div>", {"id": 'item' + index, "class":"panel-collapse collapse"}).append(
                            $("<div>").addClass("panel-body").append(subCategory)
                        )
                    ));
                });
            }
        }
    });

    $.ajax({
        type: "GET",
        url: "/api/products",
        success: function (data) {
            if (true) {
                data.forEach(product => {
                    $("#features-items").append(
                        $("<div>").addClass("col-sm-2").append(
                            $("<div>").addClass("product-image-wrapper").append(
                                $("<div>").addClass("single-products").append(
                                    $("<div>").addClass("productinfo text-center").append(
                                        $("<img>").attr("src","/static/images/products/sensor.jpg"),
                                        $("<h2>").text(product.price),
                                        $("<p>").text(product.name),
                                        $("<a>", {
                                            "class": "btn btn-default add-to-cart",
                                            "href" : product.link
                                        }).append(
                                            $("<i>").addClass("fa fa-shopping-cart").text("Thêm vào giỏ")
                                        )
                                    ),
                                    $("<div>").addClass("product-overlay").append(
                                        $("<h2>").text(product.price),
                                        $("<p>").text(product.name),
                                        $("<a>", {
                                            "class": "btn btn-default add-to-cart",
                                            "href" : product.link
                                        }).append(
                                            $("<i>").addClass("fa fa-shopping-cart").text("Thêm vào giỏ")
                                        )
                                    )
                                ),
                                // $("<div>").addClass("choose").append(
                                //     $("<ul>").addClass("nav nav-pills nav-justified").append(
                                //         $("<li>").append(
                                //             $("<a>").attr("href", "#").append(
                                //                 $("<i>").addClass("fa fa-plus-square").text("Add to wishlist")
                                //             ),
                                //             $("<a>").attr("href", "#").append(
                                //                 $("<i>").addClass("fa fa-plus-square").text("Add to compare")
                                //             )
                                //         )
                                //     )
                                // )
                            )
                        )
                    );
                })
            }
            $("#contactPhoneNumber").text(data.PhoneNumber);
            $("#contactEmail").text(data.Email);
        }
    });

});
