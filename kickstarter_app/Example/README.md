# Different templates

This example demonstrates how using an API and Javascript allows us to easily change the actual layout of the page.

## Testing the post request

## Templates

### Common files

```bash
lr.pkl               -- pickle file for model
predictor_api.py     -- python code for generating the object / dictionary
predictor_app.py     -- python/flask code for connecting requests to the api
static/js/model.js   -- javascript code for making requests to flask, and update the page
```

#### Simplest example

Extra files
```bash
templates/predictor_javascript_simple.html
```

This is close to a duplicate of the flask app using forms.

#### Using sliders
```bash
templates/predictor_javascript_sliders.html
```

Changes form to sliders. This can be done with forms as well. The new piece is that the page now dynamically responds -- there is no need to click submit. Forms always need to be submitted, and cannot dynamically update. This is also relatively easy to understand.

#### Bootstrap
```bash
templates/predictor_javascript_bootstrap.html
static/css/style.css
static/images/iris.jpg
```

Only for use of groups that have CSS experience. Can be used as a template for more professional looking apps. It also has dynamic updating.

#### Graphical sliders
```bash
templates/predictor_javascript_slider_graph.html
static/css/style.css
static/css/graph_style.css
statis/js/graph.js
```

This has a _lot_ advanced javascript methods, and uses CSS. It basically implements a D3-like graph in CSS.

## Summary

We can change templates, or change to completely different frontend platform (e.g. React, Angular, et cetera). That is typically what the web developers at your company will do. The only piece likely to survive is the POST request and routes.

We cannot make the Jinja templates transfer gracefully to React or Angular. We can take the output object from the `/predict_api` route, and process them in any javascript framework.
