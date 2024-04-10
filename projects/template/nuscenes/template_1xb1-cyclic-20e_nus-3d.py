_base_ = ['../../../../configs/_base_/default_runtime.py']
custom_imports = dict(
    imports=['projects.example_project.dummy'], allow_failed_imports=False)


_base_.model.backbone.type = 'DummyResNet'
