if __name__ == "__main__":
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Simple YouTube Comment extractor")
    parser.add_argument("url", help="The YouTube video full URL")
    parser.add_argument("-l", "--limit", type=int, help="Number of maximum comments to extract, helpful for longer videos")
    parser.add_argument("-o", "--output", help="Output JSON file, e.g data.json")
    # parse passed arguments
    args = parser.parse_args()
    limit = args.limit
    output = args.output
    url = args.url
    from pprint import pprint
    for count, comment in enumerate(get_comments(url)):
        if limit and count >= limit:
            # break out of the loop when we exceed limit specified
            break
        if output:
            # write comment as JSON to a file
            with open(output, "a") as f:
                # begin writing, adding an opening brackets
                if count == 0:
                    f.write("[")
                f.write(json.dumps(comment, ensure_ascii=False) + ",")
        else:
            pprint(comment)
            print("="*50)
    print("total comments extracted:", count)
    if output:
        # remove the last comma ','
        with open(output, "rb+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
        # add "]" to close the list in the end of the file
        with open(output, "a") as f:
            print("]", file=f)