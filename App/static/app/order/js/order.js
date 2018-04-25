$(function () {
    $("#alipay").click(function () {
        var order_id = $(this).attr("orderid");

        console.log(order_id);

        $.getJSON("/axf/changeorderstatus/", {"status":"1", "order_id":order_id},function (data) {
            console.log(data);

            if (data["status"] == "200"){
                window.open("/axf/mine/", target="_self");
            }


        })

    })
})