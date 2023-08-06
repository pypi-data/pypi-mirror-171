<p align="center">
  <img src="https://github.com/dwreeves/statelit/workflows/tests/badge.svg">
  <img src="https://github.com/dwreeves/statelit/workflows/docs/badge.svg">
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/dwreeves/statelit/main/docs/src/img/statelit-logo.png">
</p>
<p align="center">
    <em>Easy state management in Streamlit with Pydantic.</em>
</p>

---

## `StatelitModel` Attributes and Methods

The following attributes and methods are part of the public API and are considered stable.

### `StatelitModel().pydantic_obj`

Pydantic object being used by the `StatelitModel()`.

### `StatelitModel().widget()`

Render a single widget for a single field.

**Parameters:**

* `field_name: str` **(required)** - String name of the field to render a widget for.
* `key_suffix: Optional[str] = None` - Suffix to apply to the state key.
* `run_post_callback: bool = True` - If true, run the "post callback" for this field before returning a value.
* `**kwargs` - Additional keyword arguments that will be passed to the Streamlit callback.

**Returns:** (`Any`) The value output by the Streamlit callback (i.e. the value of the widget), after running the post callback if `run_post_callback` is True.

### `StatelitModel().form()`

Renders _all_ widgets for the entire Pydantic `BaseModel`. Widgets are rendered in the order they're defined in the model.

**Parameters:**

* `key_suffix: Optional[str] = None` - Suffix to apply to the state key.
* `exclude: Optional[List[str]] = None` - Which field names to exclude from rendering.
* `**kwargs` - Additional keyword arguments that will be passed to the Streamlit callback.

**Returns:** (`pydantic.BaseModel`) The Pydantic model object, `pydantic_obj`.

### `StatelitModel().code()`

Renders Markdown syntax highlighted version of the JSON state.

**Returns:** (`str`) JSON representation of the state.

### `StatelitModel().text_area()`

Renders the JSON state as a text field. The JSON can be modified, and changing its value will update all other fields to match.

**Parameters:**

* `key_suffix: Optional[str] = None` - Suffix to apply to the state key.
* `exclude: Optional[List[str]] = None` - Which field names to exclude from rendering.
* `**kwargs` - Additional keyword arguments that will be passed to the Streamlit callback.

**Returns:** (`str`) The output of the text widget, which should be a JSON representation of the state.

### `StatelitModel().lazy_text_area()`

Renders the JSON state as a "lazy" text field. The JSON can be modified, but changes won't be saved until the "Apply" button is pressed.

**Parameters:**

* `key_suffix: Optional[str] = None` - Suffix to apply to the state key.
* `exclude: Optional[List[str]] = None` - Which field names to exclude from rendering.
* `**kwargs` - Additional keyword arguments that will be passed to the Streamlit callback.

**Returns:** (`str`) The output of the text widget, which should be a JSON representation of the state.


## Types

The following implementations are considered stable:

|Type|Widget|Notes|
|---|---|---|
|`float`|`st.number_input`||
|`int`|`st.number_input`||
|`str`|`st.text_input` or `st.text_area`|`st.text_area` is used if the default value contains a `\n`; otherwise, `st.text_input` is used.|
|`enum.Enum`|`st.selectbox`|`st.radio` is also a good choice; set the `streamlit_widget` kwarg in the `Field()` to use that.|
|`datetime.date`|`st.date_input`||
|`datetime.time`|`st.time_input`||
|`pydantic.ConstrainedInt`|`st.slider`|Used when both `ge`/`gt` and `le`/`lt` are set; otherwise, use `st.number_input`|
|`pydantic.ConstrainedFloat`|`st.slider`|Used when both `ge`/`gt` and `le`/`lt` are set; otherwise, use `st.number_input`|
|`pydantic.color.Color`|`st.color_picker`|Colors are always converted to hex values.|

The following implementations are considered **experimental** and are potentially subject to some future changes:

|Type|Widget|Notes|
|---|---|---|
|`datetime.datetime`|`st.date_input`|Time component is always cast to `00:00:00`. For true datetimes, at the moment, it is suggested you use separate `datetime.date` and `datetime.time`s and manually combine them.|

## Notes on internals

Most users do not need this.

Note that the API is under development, and this may change as the project is developed. None of this is considered part of the public API.

### `StatefulObject` class

The `StatefulObject` class consists of shared internals for both model and field instances.

There are three types of state: `base`, `replicated`, and `lazy`:

* `base` state is the source of truth for all state.
* `replicated` state is always kept in sync with base state. If `replicated` state changes, then `base` state is updated.
* `lazy` state is updated when `base` state updates, but changes to lazy state will not update the base state by itself (for example, updating a lazy-state text field does not update base state, but a button may trigger a callable that updates the base state from the lazy state).

State is represented by keys associated with each object. Note that keys are by default assigned automatically. If you want to support more dynamic rendering (that makes when widgets are rendered non-deterministic), please set a `key_suffix=`.

`StatefulObject`s also have methods that allow for conversion between Statelit and Pydantic called `to_statelit` and `to_pydantic`.

### FieldFactory




# Trademark & Copyright

Streamlit is a trademark of Streamlit Inc.

This package is **unaffiliated** with Streamlit Inc. and Pydantic.
