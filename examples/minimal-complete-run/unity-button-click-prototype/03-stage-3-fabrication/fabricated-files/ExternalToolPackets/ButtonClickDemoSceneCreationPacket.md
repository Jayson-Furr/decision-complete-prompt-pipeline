# External Unity Editor Packet — ButtonClickDemo Scene

Create a Unity scene named `ButtonClickDemo.unity`.

Required hierarchy:

```text
ButtonClickDemoScene
  Main Camera
  UI Document
    Source Asset: Assets/_Project/UI/UXML/ButtonClickDemo.uxml
    Panel Settings: project default or explicitly selected panel settings
    Component: ButtonClickCounter
```

Validation required in Unity Editor:

- UXML imports without errors.
- USS imports and applies to the UI document.
- ButtonClickCounter compiles.
- Pressing the button increments the visible counter.
