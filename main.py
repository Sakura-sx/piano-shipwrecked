import badge


# FOR NOW IT IS THE BADGE APP

class App(badge.BaseApp):
    def on_open(self) -> None:
        badge.buzzer.tone(440, 1)
    
    def render_display(self, contact) -> None:
        badge.display.fill(1)  # Clear the display
        
        # text rendering: decide on a font size and line breaks for the name
        # if the name has no spaces, go as low as font size 32 before inserting hyphens where needed
        # if the name has spaces, break at the middlemost space first, then the rest of the spaces, then insert hyphens as needed
        max_handle_chars = 200 // badge.display.nice_fonts[24].max_width
        handle_wrapped = [f"@{contact.handle}"[i:i + max_handle_chars] for i in range(0, len(contact.handle) + 1, max_handle_chars)]
        self.logger.debug(f"Wrapped handle: {handle_wrapped}")
        name_space_avail = 200 - 24 - (len(handle_wrapped) * 24)
        font, name = self.decide_name_size(contact.name, name_space_avail)
        self.logger.debug(f"In space {name_space_avail}, using size {font.height} with {name}")
        name_height = font.height * (name.count('\n') + 1)
        badge.display.nice_text(name, 0, 0, font=font, color=0, rot=0, x_spacing=0, y_spacing=0)
        badge.display.nice_text(f"{contact.pronouns}", 0, name_height, font=24, color=0, rot=0, x_spacing=0, y_spacing=0)
        badge.display.nice_text(f"0x{contact.badge_id:0>4x}", 200-badge.display.nice_fonts[24].max_width*6, name_height, font=24, color=0, rot=0, x_spacing=0, y_spacing=0)
        badge.display.nice_text('\n'.join(handle_wrapped), 0, name_height + 24, font=24, color=0, rot=0, x_spacing=0, y_spacing=0)
        badge.display.show()
    
    def decide_name_size(self, name: str, y_space_available=130):
        """
        Decide the best size and line breaks for the name.
        Tries to use as large of a font as possible while not breaking the name in weird places (if possible).
        """
        font = None
        max_chars_for_sizes = {size: badge.display.width // font.max_width for size, font in badge.display.nice_fonts.items()}
        for size, max_chars in sorted(max_chars_for_sizes.items(), key=lambda x: x[0], reverse=True):
            if size < 24:
                # we don't want to use sizes smaller than 24 for names
                continue
            if len(name) <= max_chars and size <= y_space_available:
                font = badge.display.nice_fonts[size]
                break
            elif ' ' in name:
                # If the name has spaces, break at the middlemost space first
                parts = name.split(' ')
                mid = len(parts) // 2
                test_name = ' '.join(parts[:mid]) + '\n' + ' '.join(parts[mid:])
                if max(len(part) for part in test_name.split('\n')) <= max_chars and 2 * size <= y_space_available:
                    name = test_name
                    font = badge.display.nice_fonts[size]
                    break
                else:
                    # try breaking on all spaces
                    lines_available = y_space_available // size
                    if len(parts) > lines_available:
                        # this many lines will run the rest of the text off the screen
                        continue
                    if max(len(part) for part in parts) <= max_chars and len(parts) * size <= y_space_available:
                        name = '\n'.join(parts)
                        font = badge.display.nice_fonts[size]
                        break
        if not font:
            # we have to hyphenate
            # we have 130 pixels, figure out how big the font can be while fitting the name
            for size, max_chars in sorted(max_chars_for_sizes.items(), key=lambda x: x[0], reverse=True):
                lines_available = y_space_available // size
                if len(name) // lines_available <= (max_chars - 1):
                    font = badge.display.nice_fonts[size]
                    name = '-\n'.join(name[i:i + max_chars - 1] for i in range(0, len(name), max_chars - 1))
                    break
        if not font:
            # just use the smallest font and cut off the rest
            font = badge.display.nice_fonts[18]
            name = '-\n'.join([name[i:i + 10] for i in range(0, len(name), 10)][:7])
        return font, name


    def loop(self) -> None:
        # 440.0	466.2	493.9   523.3	554.4	587.3	622.3	659.3	698.5	740.0	784.0	830.6	880.0	932.3	987.8
        if badge.input.get_button(badge.input.Buttons.SW4):
            badge.buzzer.tone(440, 1)
        elif badge.input.get_button(badge.input.Buttons.SW5):
            badge.buzzer.tone(466, 1)
        elif badge.input.get_button(badge.input.Buttons.SW6):
            badge.buzzer.tone(494, 1)
        elif badge.input.get_button(badge.input.Buttons.SW7):
            badge.buzzer.tone(523, 1)
        elif badge.input.get_button(badge.input.Buttons.SW8):
            badge.buzzer.tone(554, 1)
        elif badge.input.get_button(badge.input.Buttons.SW9):
            badge.buzzer.tone(587, 1)
        elif badge.input.get_button(badge.input.Buttons.SW10):
            badge.buzzer.tone(622, 1)
        elif badge.input.get_button(badge.input.Buttons.SW11):
            badge.buzzer.tone(659, 1)
        elif badge.input.get_button(badge.input.Buttons.SW12):
            badge.buzzer.tone(699, 1)
        elif badge.input.get_button(badge.input.Buttons.SW13):
            badge.buzzer.tone(740, 1)
        elif badge.input.get_button(badge.input.Buttons.SW14):
            badge.buzzer.tone(784, 1)
        elif badge.input.get_button(badge.input.Buttons.SW15):
            badge.buzzer.tone(831, 1)
        elif badge.input.get_button(badge.input.Buttons.SW16):
            badge.buzzer.tone(880, 1)
        elif badge.input.get_button(badge.input.Buttons.SW17):
            badge.buzzer.tone(932, 1)
        elif badge.input.get_button(badge.input.Buttons.SW18):
            badge.buzzer.tone(988, 1)
        else:
            pass