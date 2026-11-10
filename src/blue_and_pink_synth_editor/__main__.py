from multiprocessing import set_start_method, freeze_support
from blue_and_pink_synth_editor.BlueAndPinkSynthEditorApp import BlueAndPinkSynthEditorApp

def main():
    freeze_support()
    set_start_method('spawn', force=True)
    BlueAndPinkSynthEditorApp().run()

if __name__ == '__main__':
    main()
