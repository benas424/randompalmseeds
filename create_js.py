import scrape


def main():
    with open("web_content/generated.js", "w") as output:
        output.write("function openRandom() {\n")

        output.write("  const links = [")

        links = scrape.find_all_plants()
        is_first = True
        for link in links:
            if not is_first:
                output.write(",")
            else:
                is_first = False
            output.write("\n  \"")
            output.write(link)
            output.write("\"")
        output.write("];\n")

        output.write("  let pick = links[Math.floor(Math.random()*links.length)];\n")

        output.write("  window.open(pick);")

        output.write("}")


if __name__ == "__main__":
    main()
