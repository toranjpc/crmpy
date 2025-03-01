// Initialize the formio builder configuration (optional)
// Default cartegories: basic, advanced, layout, data
const options = {
  builder: {
    basic: {
      // We can change the title of a category...
      title: 'Basic'
    },
    layout: {
      // ... or change its position...
      weight: 100
    },
    // ... and even create custom categories
    custom: {
      title: 'Custom'
    }
  }
};

// Initialize the form.io form JSON object
const form = {
  components: [
    {
      key: 'textfield',
      type: 'textfield',
      validate: {
        required: true
      }
    },
    {
      key: 'datetime',
      type: 'datetime'
    },
    {
      key: 'submit',
      type: 'button',
      theme: 'primary'
    }
  ]
};

const formio = {
  builder: null,
  form: null
};

// Initialize the formio form instance
Formio.createForm(document.getElementById('formio-form'), form)
  .then((instance) => {
    formio.form = instance;
});

// Initialize the formio builder instance
Formio.builder(document.getElementById('formio-builder'), form, options)
  .then((instance) => {
    formio.builder = instance;
    // Define the on render event of the formio builder instance
    formio.builder.on('render', () => {
      // Update the formio form object and re render the form
      formio.form.form = form;
      formio.form.render();
      
      // Update the json code using Prism.js
      document.querySelector('code').innerHTML = Prism.highlight(JSON.stringify(form, null, 2), Prism.languages.json, 'json');
    });
    document.querySelector('code').innerHTML = Prism.highlight(JSON.stringify(form, null, 2), Prism.languages.json, 'json');
  });