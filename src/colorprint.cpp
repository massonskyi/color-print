#include "colorprint.h"

#include <stdexcept>
#include <typeinfo>
#include <cstring>

void Colors::set_current_color(ColorPrint& cp, std::string& c){
    std::unordered_map<std::string, std::string>::const_iterator it = this->colorsDict.find(c);
    if (it != this->colorsDict.end()) {
        // cp.set_color( it->second);
    } else {
        // cout << "Unknown color" << endl;
    }
}
ColorPrint::ColorPrint(void) : color({})
{
    this->str = "";
    this->length = 0;
    this->isHighlighted = false;
    this->isUnderlined = false;
    this->isBold = false;
}

template <typename str_type>
ColorPrint::ColorPrint(
    str_type str,
    unsigned int length,
    bool isHighlighted = false,
    bool isUnderlined = false,
    bool isBold = false): color({})
{
    if (typeid(str) != typeid(std::string) || typeid(str) != typeid(char*))
    {
        throw std::runtime_error("Value must be std::string or pointer on chars");
    }

    if (typeid(str) == typeid(char *))
    {
        this->str = std::string(str);
    }
    else
    {
        this->str = str;
    }

    if (isHighlighted)
        this->isHighlighted = isHighlighted;
    else
        this->isHighlighted = false;
    if (isUnderlined)
        this->isUnderlined = isUnderlined;
    else
        this->isUnderlined = false;
    if (isBold)
        this->isBold = isBold;
    else
        this->isBold = false;
    this->length = length;
};

ColorPrint::~ColorPrint(void)
{
}

std::string ColorPrint::fstring() const{
    return this->str;
}

int ColorPrint::flen() const{
    return this->length;
}
void ColorPrint::set_color(Colors color){
    this->color = color;
}
template <typename str_type>
void ColorPrint::setString(str_type str)
{
    if (typeid(str) != typeid(std::string) || typeid(str) != typeid(char*))
    {
        throw std::runtime_error("Value must be std::string or pointer on chars");
    }

    if (typeid(str) == typeid(char *))
    {
        this->str = std::string(str);
    }
    else
    {
        this->str = str;
    }
}

void ColorPrint::create_text()
{
    std::string output = this->str;
    for(auto var : color)
    {
        
    }
    for(unsigned int i = 0; i < this->length; i++){
        output = 
    }
    if (isHighlighted)
        output = "\033[43m" + output + "\033[0m";

    if (isUnderlined)
        output = "\033[4m" + output + "\033[0m";

    if (isBold)
        output = "\033[1m" + output + "\033[0m";
    

}

void ColorPrint::clear()
{
    isHighlighted = false;
    isUnderlined = false;
    isBold = false;
}

void ColorPrint::highlight()
{
    isHighlighted = true;
}

void ColorPrint::underline()
{
    isUnderlined = true;
}

void ColorPrint::bold()
{
    isBold = true;
}
template <typename T>
T &ColorPrint::operator=(const T &other)
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    if (typeid(other) == typeid(ColorPrint))
    {
        if (this != &other)
        {
            this->str = other.fstring();
            this->length = other.flen();
            this->isHighlighted = other.isHighlighted;
            this->isUnderlined = other.isUnderlined;
            this->isBold = other.isBold;
        }
        return *this;
    }
    else {
        unsigned int len = strlen(other)
        return ColorPrint(other, len);
    }
}
template <typename T>
T ColorPrint::operator+(const T &other) const
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    if (typeid(other) == typeid(ColorPrint))
    {
        return ColorPrint(this->str + other.fstring(), this->length + other.flen());
    }
    else 
        return ColorPrint(other, strlen(other));
}
std::ostream &operator<<(std::ostream &os, const ColorPrint&cp)
{
    os << cp.fstring();
    return os;
}

template <typename T>
T ColorPrint::operator*(int n) const
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    std::string newStr = this->str;
    unsigned int newLength = this->length;

    for (int i = 1; i < n; ++i)
    {
        this->str += str;
        this->length += length;
    }

    return ColorPrint(newStr, newLength);
}

template <typename T>
T &ColorPrint::operator+=(const T &other)
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    if(typeid(other) == typeid(ColorPrint)){
        this->str =  this->str + other.fstring();
        this->length = this->length + other.flen();

        return *this;
    }
    else{
        this->str = this->str + std::string(other);
        if(typeid(other) == typeid(char *))
            this->length = this->length + strlen(other);
        else
            this->length = this->length + strlen(other.c_str());
        return *this;
    }
}

template <typename T>
bool ColorPrint::operator==(const T &other) const
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    if(typeid(other) == typeid(ColorPrint))
        return (std::string(str) == std::string(other.fstring()));
    else
        return (std::string(str) == std::string(other));
}

template <typename T>
bool ColorPrint::operator!=(const T &other) const
{
    if (typeid(other) != typeid(std::string) ||
        typeid(other) != typeid(char*) ||
        typeid(other) != typeid(ColorPrint))
    {
        throw std::runtime_error("Value must be std::string, pointer on chars or ColorPrint class");
    }
    if(typeid(other) == typeid(ColorPrint))
        return (std::string(str) != std::string(other.fstring()));
    else
        return (std::string(str) != std::string(other));
}

char ColorPrint::operator[](int index) const
{
    if (index >= 0 && index < length)
    {
        return str[index];
    }
    else
    {
        return '\0';
    }
}