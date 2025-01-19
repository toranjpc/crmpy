var richTextEditor = {
  bindEvents: function (element) {
    this.bindDesignModeToggle(element);
    this.bindToolbarButtons(element);
  },

  // bindDesignModeToggle: function (element) {
  //   $(element).find('.htmlpage').on('click', function (e) {
  //     document.designMode = 'on';
  //   });

  //   $(document.body).on('click', function (e) {
  //     var $target = $(e.target);

  //     if ($target.is('body')) {
  //       document.designMode = 'off';
  //     }
  //   });
  // },

  bindToolbarButtons: function (element) {
    $('.toolbar').on('mousedown', '.icon', function (e) {
      e.preventDefault();
      var btnId = $(e.target).attr('id');
      this.editStyle(btnId, element);
    }.bind(this));
  },

  editStyle: function (btnId, element) {
    var value = null;

    if (btnId === 'createLink') {
      if (this.isSelection(element)) value = prompt('Enter a link:');
    }

    document.execCommand(btnId, true, value);
  },

  isSelection: function (element) {
    var selection = window.getSelection();
    return selection.anchorOffset !== selection.focusOffset
  },

  init: function (element) {
    this.bindEvents(element);
  },
}

// richTextEditor.init(".textarea");
