import curses


def main(main_screen):
    main_screen.addstr(0, 0, "Press 'q' to quit...")
    main_screen.refresh()

    while True:
        c = main_screen.getch()
        if c == ord('q'):
            break


curses.wrapper(main)
