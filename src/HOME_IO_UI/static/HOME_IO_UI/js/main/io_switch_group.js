var IOSwitchGroup = function () {
    this.groupId;
    this.name;
    this.icon;
    this.ioSwitches = [];
}

$.extend(IOSwitchGroup.prototype, {
    render: function () {
        $.each(this.ioSwitches, function (index, ioSwitch) {
            ioSwitch.render();
        });
    },
    clear: function () {
        $('#ioSwitchGroupContainer').html('');
    }
});