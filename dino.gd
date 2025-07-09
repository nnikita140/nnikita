extends CharacterBody2D

const GRAVITY:int = 5000
const JUMP_SPEED:int = -1800


func _physics_process(delta):
	velocity.y += GRAVITY * delta
   
   
	move_and_slide()


func _physics_process(delta):
	if input.is_action_pressed("ui_accept"):
		velocity.y = JUMP_SPEED
		$AnimatedSprite2D.play("jump")


if is_on_floor():
	if input.is_action_pressed("ui_accept"):
		velocity.y = JUMP_SPEED
		$AnimatedSprite2D.play("jump")


if input.is_action_pressed("ui_accept"):
	velocity.y = JUMP_SPEED
	$AnimatedSprite2D.play("jump")
else:
	$AnimatedSprite2D.play("run")
