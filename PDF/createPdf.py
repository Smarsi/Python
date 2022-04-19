from fpdf import FPDF

#texto que viria de um lugar qualquer
texto = "Este é um texto de exemplo que deverá ser inserido dentro de um pdf que será gerado pela biblioteca fpdf. Qualquer texto pode ser inserido aqui."

novo_pdf = FPDF() # chamando a biblioteca

novo_pdf.add_page() # adicionando uma página dentro do documento (isso poderia estar em um laço caso fosse necessário criar várias páginas dinamicamente dependendo da necessidade)

novo_pdf.set_font('Arial', 'B', 16) # setando a fonte do texto que será inserido: neste caso para o título
novo_pdf.cell(40, 10, 'Este é meu PDF')
novo_pdf.ln(20)

novo_pdf.set_font('Arial', '', 14) # setando a fonte do texto que será inserido: neste caso para o texto
novo_pdf.multi_cell(0, 5, texto, 'C')

novo_pdf.output('Exemplo.pdf', 'F')

