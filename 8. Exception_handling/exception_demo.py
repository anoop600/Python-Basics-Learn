def banner_text(text: str = " ", screen_width: int = 80) -> None:

    """ Print a string centred, with ** either side.
  
    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """

    if len(text) > screen_width - 4:
        raise ValueError(
            "String {} is larger than specified width".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)

screen_width = 60
banner_text("*", screen_width)
banner_text("Always look on the bright side of life...", screen_width)
banner_text("If life seems jolly rotten,", screen_width)
banner_text("There's something you've forgotten!", screen_width)
banner_text("And that's to laugh and smile and dance and sing,", screen_width)
banner_text(screen_width = screen_width) #key_word_argument
banner_text("When you're feeling in the dumps,", screen_width)
banner_text("Don't be silly chumps,", screen_width)
banner_text("Just purse your lips and whistle - that's the thing!", screen_width)
banner_text("And... always look on the bright side of life...", screen_width)
banner_text("*", screen_width)
