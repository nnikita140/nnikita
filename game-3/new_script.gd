extends Node

func _on_play_pressed():
	$AnimationPlayer.play("play")
	$play_sound.play()
	$menu.stop()

func play():
	get_tree().change_scene_to_file("res://levels/level.tscn")
