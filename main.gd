extends Node

var game_running: bool = true
var speed: float


const START_SPEED: float = 3.0


func _procces(delta):
	if game_running:
		speed = START_SPEED
		$Dino.position.x += speed
		$Camera2D.position.x += speed


var screen_size: Vector2i

func _ready():
	screen_size = get_window().size


func _process(delta):
	if game_running:
		
