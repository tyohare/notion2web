import os

def list_html_files(startpath):
    """
    This function returns a list of all HTML files in the given directory
    and its subdirectories recursively.
    """
    html_files = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def print_article_content(html_file):
    """
    This function opens an HTML file, prints the file name,
    and then prints the content between the "<article" and "</article>" tags.
    """
    with open(html_file) as f:
        content = f.read()
        start_tag = '<article'
        end_tag = '</article>'
        start_index = content.find(start_tag)
        end_index = content.find(end_tag, start_index)
        if start_index != -1 and end_index != -1:
            article_content = content[start_index:end_index + len(end_tag)]
            print(f"File Name: {html_file}")
            print(article_content)
            print("=" * 80)

if __name__ == '__main__':
    startpath = '.'  # Current directory
    html_files = list_html_files(startpath)
    for html_file in html_files:
        print_article_content(html_file)
import os
import shutil

def list_html_files(startpath):
    """
    This function returns a list of all HTML files in the given directory
    and its subdirectories recursively.
    """
    html_files = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def extract_article_content(html_file):
    """
    This function extracts the content between the "<article" and "</article>" tags
    from an HTML file and returns it as a string.
    """
    with open(html_file) as f:
        content = f.read()
        start_tag = '<article'
        end_tag = '</article>'
        start_index = content.find(start_tag)
        end_index = content.find(end_tag, start_index)
        if start_index != -1 and end_index != -1:
            article_content = content[start_index:end_index + len(end_tag)]
            return article_content
    return None

def merge_content(html_file, article_content):
    """
    This function merges the extracted article content into a new HTML file.
    It first copies the contents of a specified file into the new file,
    then finds the positions of the <main> and </main> tags and adds the extracted
    article content between them.
    """
    filename = os.path.splitext(html_file)[0]
    output_file = filename + '.html' # + '_merged.html'
    source_file = 'test.html'
    shutil.copy(source_file, output_file)
    with open(output_file, 'r+') as f:
        content = f.read()
        start_tag = '<main class="main">'
        end_tag = '</main>'
        start_index = content.find(start_tag)
        end_index = content.find(end_tag, start_index)
        if start_index != -1 and end_index != -1:
            f.seek(end_index - len(end_tag))
            end_content = content[end_index:]
            f.seek(start_index + len(start_tag))
            f.write(article_content)
            f.write(end_tag)
            f.write(end_content)
    return output_file




if __name__ == '__main__':
    startpath = '.'  # Current directory
    html_files = list_html_files(startpath)
    for html_file in html_files:
        article_content = extract_article_content(html_file)
        if article_content:
            output_file = merge_content(html_file, article_content)
            print(f"Merged file created: {output_file}")
