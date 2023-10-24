# todo add doc strings and comments and stuff so future you and other people don't struggle to read your spaghetti code
import scalestuff
import modestuff
import intervalstuff

main_menu_prompt = ('Main Menu\n'
                    'Program options:\n'
                    '  (Show) Displays concepts.\n'
                    '  (Hide) Removes concept from final review.\n'
                    'Good to do for accidental searches.\n'
                    '  (Print) Prints list that documents what the user\n'
                    'has searched to review areas of focus for practice.\n'
                    '  (Quit) Terminates program.\n'
                    '\n'
                    'Enter input: ')

main_menu_options = ['Show', 'Hide', 'Print', 'Quit']

table_of_contents_prompt = ('Concept options:\n'
                            '  (Scales) Displays Scales.\n'
                            '  (Modes) Displays Modes.\n'
                            '  (Intervals) Displays basic Interval information.\n'
                            '  (More Intervals) Displays information about Circle of Fifths/Fourths, Order of\n'
                            'Sharps/Flats, etc.\n'
                            '\n'
                            'Enter concept: ')

table_of_contents = ['Scales', 'Modes', 'Intervals', 'More Intervals']

vocab = ['Show', 'Hide', 'Print', 'Quit', 'Scales', 'Modes', 'Intervals', 'More Intervals', 'Major', 'Major Pentatonic',
         'Minor', 'Melodic Minor', 'Harmonic Minor', 'Minor Pentatonic', 'Ionian', 'Dorian', 'Phrygian', 'Lydian',
         'Mixolydian', 'Aeolian', 'Locrian', 'Interval Basics', 'Chord Basics', 'Chord Progressions', 'Arpeggio Basics',
         'Circles', 'Orders', 'Scale Degrees']  # todo Convert into dict for a 'help' command

selected_topics = {}


def validate(command):
    if command == '':
        print('Enter any command below to continue.')
        return
    elif command not in vocab:
        print('Unknown, please check for misspelling.')
        return


def hide_check():
    if not selected_topics:
        print('No topics are available for review.')
        return
    elif selected_topics:
        hide()
        return


def hide():
    topic = input('Enter topic you wish to remove from topic review: ').strip().lower().title()
    if topic in selected_topics:
        del selected_topics[topic]
        return
    else:
        print('Topic is either misspelled or has not been searched for.')
        return


def print_check():
    if not selected_topics:
        print('Nothin\' here.')


def topic_location():
    for key, value in selected_topics.items():
        print(f'{key} --> {value}')


def main():
    print("Welcome to the Rizzless Guitar Guide!\n")
    user_input = input(main_menu_prompt).strip().lower().title()  # Figure out how to delete all the starting print()s

    while user_input != 'Quit':
        if user_input == 'Show':
            print()
            user_input = input(table_of_contents_prompt).strip().lower().title()
            continue
        elif user_input == 'Scales':
            print()
            user_input = input(scalestuff.scales_prompt).strip().lower().title()
            continue
        elif user_input == 'Major':
            print()
            print(scalestuff.major_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Major Pentatonic':
            print()
            print(scalestuff.major_penta_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Minor':
            print()
            print(scalestuff.minor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Melodic Minor':
            print()
            print(scalestuff.melminor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Harmonic Minor':
            print()
            print(scalestuff.harminor_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Minor Pentatonic':
            print()
            print(scalestuff.minor_penta_scale_prompt)
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Scale Degrees':
            print()
            scalestuff.formatted_scale_degrees()
            selected_topics[user_input] = 'Scale'
        elif user_input == 'Modes':
            print()
            user_input = input(modestuff.modes_prompt).strip().lower().title()
            continue
        elif user_input == 'Ionian':
            print()
            print(modestuff.ionian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Dorian':
            print()
            print(modestuff.dorian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Phrygian':
            print()
            print(modestuff.phrygian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Lydian':
            print()
            print(modestuff.lydian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Mixolydian':
            print()
            print(modestuff.mixolydian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Aeolian':
            print()
            print(modestuff.aeolian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Locrian':
            print()
            print(modestuff.locrian_mode_prompt)
            selected_topics[user_input] = 'Mode'
        elif user_input == 'Intervals':
            print()
            user_input = input(intervalstuff.interval_menu).strip().lower().title()
            continue
        elif user_input == 'Interval Basics':
            print()
            print(intervalstuff.interval_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Chord Basics':
            print()
            print(intervalstuff.chord_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Chord Progressions':
            print()
            print(intervalstuff.chord_progs)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'Arpeggio Basics':
            print()
            print(intervalstuff.arpeggio_basics)
            selected_topics[user_input] = 'Interval'
        elif user_input == 'More Intervals':
            print()
            user_input = input(intervalstuff.more_intervals_menu).strip().lower().title()
            continue
        elif user_input == 'Circles':
            print()
            print(intervalstuff.circles_prompt)
            selected_topics[user_input] = 'More Intervals'
        elif user_input == 'Orders':
            print()
            print(intervalstuff.orders_prompt)
            selected_topics[user_input] = 'More Intervals'
        elif user_input == 'Hide':
            print()
            hide_check()
            print()
        elif user_input == 'Print':
            print()
            print_check()
            topic_location()
        else:
            validate(user_input)

        user_input = input(main_menu_prompt[26:]).strip().lower().title()


if __name__ == '__main__':
    main()

# todo create tests
