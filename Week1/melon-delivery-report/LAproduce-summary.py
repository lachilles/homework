print "Day 1"

the_file = open("um-deliveries-20140519.txt")

def delivery_info(the_file):
    for line in the_file.readlines():
        line = line.strip()
        #print(line)
        words = line.split("|")
        # for word in words:
        #     print("    ",word)

        melon = words[0]
        count = words[1]
        amount = words[2]


        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)

delivery_info(the_file)

the_file.close()

print "Day 2"

the_file = open("um-deliveries-20140520.txt")

delivery_info(the_file)

the_file.close()


print "Day 3"

the_file = open("um-deliveries-20140521.txt")

delivery_info(the_file)

the_file.close()
