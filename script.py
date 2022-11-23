import sys

vars = ['square', 'circle']

class CreateSVG:
    def __init__(self, name, size, color, filename) -> None:
        self.size = size
        self.color = color
        self.name = name
        self.filename = filename

    @property
    def create(self):
        if(str(self.name).lower()) in vars:
            if str(self.name).lower() == 'circle':
                text = f"""<svg version="1.1"
                    baseProfile="full"
                    width="{double_sile}" height="{double_sile}"
                    xmlns="http://www.w3.org/2000/svg">
                <circle cx="{self.size}" cy="{self.size}" r="{self.size}" fill="{self.color}"/>
                </svg>
                """
                with open(f'{self.filename}', 'w', encoding='utf-8') as file:
                    file.write(text)
            if str(self.name).lower() == 'square':  
                double_sile = int(self.size)*2 
                text = f"""<svg version="1.1"
                    xmlns="http://www.w3.org/2000/svg">
                <rect x="100" y="100" width="{self.size}" height="{self.size}" stroke="{self.color}" fill="{self.color}" stroke-width="5"/>
                </svg>
                """  
                with open(f'{self.filename}', 'w', encoding='utf-8') as file:
                    file.write(text)
        else:
            print("enter square or circle")

            
def main(name, size, color, filename):
    CreateSVG(name, size, color, filename).create

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])