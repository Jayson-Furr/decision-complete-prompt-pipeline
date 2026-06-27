# Unity Editor Validation Checklist

Run these checks in the target Unity version before release or implementation handoff:

- Open the project in the selected Unity version.
- Confirm UXML import succeeds.
- Confirm USS import succeeds.
- Attach the UXML to a UIDocument in a scene.
- Attach `ButtonClickCounter` to the same GameObject as the UIDocument.
- Enter Play Mode.
- Confirm initial text reads `Count: 0`.
- Click the button once.
- Confirm text reads `Count: 1`.
- Run Edit Mode tests.
- Build only after explicit authorization.
