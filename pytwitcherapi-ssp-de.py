        if m.text == "command schere":
                i = randint(1, 3)
                print(i)
                
                if i == 1:
                    client.send_msg("Schere, unentschieden! DansGame")

                if i == 2:
                    client.send_msg("Stein, ich habe gewonnen! PogChamp")

                if i == 3:
                     client.send_msg("Papier, du hast gewonnen! BibleThump")

        if m.text == "command stein":
                i = randint(1, 3)
                print(i)
                
                if i == 1:
                    client.send_msg("Schere, du hast gewonnen! BibleThump")

                if i == 2:
                    client.send_msg("Stein, unentschieden! DansGame")

                if i == 3:
                     client.send_msg("Papier, ich habe gewonnen! PogChamp")

        if m.text == "command papier":
                i = randint(1, 3)
                print(i)
                
                if i == 1:
                    client.send_msg("Schere, ich habe gewonnen! PogChamp")

                if i == 2:
                    client.send_msg("Stein, du hast gewonnen! BibleThump")

                if i == 3:
                     client.send_msg("Papier, unentschieden! DansGame")

        if m.text == "command ssp help":
            client.send_msg("Hier die Regeln: https://pastebin.com/14yU0p8j")