def banner_text(text = " ", screen_width = 80):
    """[Read text and makes creates a wonderfull banner]

    Args:
        text (str, optional): [description]. Defaults to " ".
        screen_width (int, optional): [description]. Defaults to 80.

    Raises:
        ValueError: [if screen width is less than length of text then will create Value Error Exception]
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
