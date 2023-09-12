#ifndef COLORPRINT_H
#define COLORPRINT_H


#include <iostream>
#include <string>
#include <unordered_map>
struct Colors {
public:
    std::unordered_map<std::string, std::string> colorsDict {
        { "BLACK", "\033[30m" },
        { "RED", "\033[31m" },
        { "GREEN", "\033[32m" },
        { "YELLOW", "\033[33m" },
        { "BLUE", "\033[34m" },
        { "MAGENTA", "\033[35m" },
        { "CYAN", "\033[36m" },
        { "WHITE", "\033[97m" },
        { "RESET", "\033[0m" },
        { "BACKGROUND_BLACK", "\033[40m" },
        { "BACKGROUND_RED", "\033[41m" },
        { "BACKGROUND_GREEN", "\033[42m" },
        { "BACKGROUND_YELLOW", "\033[43m" },
        { "BACKGROUND_BLUE", "\033[44m" },
        { "BACKGROUND_MAGENTA", "\033[45m" },
        { "BACKGROUND_CYAN", "\033[46m" },
        { "BACKGROUND_WHITE", "\033[47m" }
    };


    Colors(){};
    void set_current_color(ColorPrint& cp, std::string& c);
};

class ColorPrint
{
public:
    template <typename T>
    ColorPrint(
        T,
        unsigned int,
        bool,
        bool,
        bool);
    ColorPrint(void);
    ~ColorPrint(void);

    std::string fstring() const;

    int flen() const;

    void set_color(Colors color);
    template <typename T>
    void setString(T);

    void create_text();
    void clear();
    void highlight();
    void underline();
    void bold();
    template <typename T>
    T &operator=(const T &);

    template <typename T>
    T operator+(const T &) const;

    friend std::ostream &operator<<(std::ostream &, const ColorPrint&);

    template <typename T>
    T operator*(int) const;

    template <typename T>
    T &operator+=(const T &);

    template <typename T>
    bool operator==(const T &) const;

    template <typename T>
    bool operator!=(const T &) const;

    char operator[](int) const;

private:
    Colors color;
    std::string str;
    unsigned int length;
    bool isHighlighted;
    bool isUnderlined;
    bool isBold;
};

#endif /*END COLORPRINT_H*/