hero_sprite: Sprite = sprites.create(assets.image("""Grayson"""),
    SpriteKind.player)
def on_a_pressed():
    animation.run_image_animation(hero_sprite,
        assets.animation("""Gray"""), 500, True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
def on_b_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL,
        hero_sprite)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)
