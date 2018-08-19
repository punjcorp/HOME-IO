var IOSwitch = function () {
    this.switchId;
    this.name;
    this.icon;
    this.state;
}

$.extend(IOSwitch.prototype, {
    toggle: function () {
        var postedSwitch = this;
        var token = $("meta[name='_csrf']").attr("content");
        var formdata = JSON.stringify(postedSwitch);
        // AJAX call here and refresh the sell item page with receipt printing
        $.ajax({
            url: toggle_io_switch_url,
            type: 'POST',
            cache: false,
            data: formdata,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                postedSwitch.processResponse(response);
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRF-TOKEN', token)
            }
        });

    },
    render: function () {

    },
    updateActionResponse: function (response) {
        this.switchId = response.ioSwitch.switchId;
        this.name = response.ioSwitch.name;
        this.icon = response.ioSwitch.icon;
        this.state = response.ioSwitch.state;
    },
    processResponse: function (response) {
        this.updateActionResponse(response);
        this.render();
    }

});