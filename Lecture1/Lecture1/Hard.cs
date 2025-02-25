using System;
using System.Text;

class ArithmeticInterpreter
{
    private string input;
    private int pos;

    public ArithmeticInterpreter(string input)
    {
        this.input = input;
        this.pos = 0;
    }

    public int Calculate()
    {
        int result = AddSubtract();
        if (pos < input.Length)
        {
            throw new Exception("ERROR");
        }
        return result;
    }

    private int AddSubtract()
    {
        int result = MultiplyDivide();
        while (pos < input.Length)
        {
            char op = input[pos];
            if (op == '+' || op == '-')
            {
                pos++;
                int term = MultiplyDivide();
                if (op == '+')
                {
                    result += term;
                }
                else
                {
                    result -= term;
                }
            }
            else
            {
                break;
            }
        }
        return result;
    }

    private int MultiplyDivide()
    {
        int result = GetNumberOrParentheses();
        while (pos < input.Length)
        {
            char op = input[pos];
            if (op == '*' || op == '/')
            {
                pos++;
                int factor = GetNumberOrParentheses();
                if (op == '*')
                {
                    result *= factor;
                }
                else
                {
                    if (factor == 0)
                    {
                        throw new Exception("ERROR");
                    }
                    result /= factor;
                }
            }
            else
            {
                break;
            }
        }
        return result;
    }

    private int GetNumberOrParentheses()
    {
        if (pos < input.Length && input[pos] == '(')
        {
            pos++;
            int result = AddSubtract();
            if (pos >= input.Length || input[pos] != ')')
            {
                throw new Exception("ERROR");
            }
            pos++;
            return result;
        }
        else
        {
            return ReadNumber();
        }
    }

    private int ReadNumber()
    {
        int start = pos;
        while (pos < input.Length && char.IsDigit(input[pos]))
        {
            pos++;
        }
        if (start == pos)
        {
            throw new Exception("ERROR");
        }
        return int.Parse(input.Substring(start, pos - start));
    }
}

class Hard
{
    static void Main(string[] args)
    {
        string[] inputs = {
            "2",
            "2*(3+5)",
            "15-2**7",
            "20/2/2",
            "3+2*1"
        };

        foreach (var input in inputs)
        {
            try
            {
                var interpreter = new ArithmeticInterpreter(input);
                int result = interpreter.Calculate();
                Console.WriteLine(result);
            }
            catch (Exception ex)
            {
                Console.WriteLine("ERROR");
            }
        }
    }
}