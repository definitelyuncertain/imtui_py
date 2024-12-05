import imtui_py
# This hack is an attempt to make the code slightly more
# portable to other ImGui backends
imgui = imtui_py

imgui.create_context()
imtui_py.imtui_init()

while(True):
	imtui_py.imtui_start_new_frame()

	imgui.set_next_window_pos(imgui.Vec2(55, 5), imgui.COND_ONCE)
	imgui.set_next_window_size(imgui.Vec2(20, 20), imgui.COND_ONCE)
	imgui.begin("Your first window!")
	imgui.text("Hello world!")
	if imgui.button("Exit Program", imgui.Vec2(imgui.get_content_region_avail().x,2)):
		break;
	imgui.end()

	imgui.render()

	imtui_py.imtui_finish_frame()

imtui_py.imtui_cleanup()