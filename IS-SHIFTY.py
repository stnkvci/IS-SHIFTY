from game import game
import sys
import traceback

if __name__ == '__main__':
    try:
        while game.running:
            game.current_menu.display_menu()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n{'='*60}")
        print("GAME CRASHED - Error Details:")
        print(f"{'='*60}")
        print(f"Error: {e}")
        print(f"\nFull traceback:")
        traceback.print_exc()
        print(f"{'='*60}")
        sys.exit(1)
