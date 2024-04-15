let hero_sprite = sprites.create(assets.image`Grayson`, SpriteKind.Player)
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    animation.runImageAnimation(hero_sprite, assets.animation`Gray`, 500, true)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    animation.stopAnimation(animation.AnimationTypes.All, hero_sprite)
})
