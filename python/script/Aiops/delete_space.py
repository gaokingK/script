"""
将多行内容变成一行并粘贴到剪贴板，按q退出
# pyperclip # python剪贴板




"""
import pyperclip


def delete_space():
    lines = []
    while True:
        line = input("Enter a line (or 'q' to quit): ")
        if line.strip() == '':
            output_line = ' '.join(lines)
            # pyperclip.copy(output_line)
            output_line = output_line.replace("或",  "").replace("且", "\n且\n")
            pyperclip.copy(output_line)
            print(output_line)
            lines = []
        elif line.lower() == "q":
            output_line = ' '.join(lines)
            output_line = output_line.replace("或",  "").replace("且", "\n且\n")

            pyperclip.copy(output_line)
            print(output_line)
            break
        lines.append(line)


if __name__ == "__main__":
    delete_space()
