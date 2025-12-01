# Simulador-Semaforo-Tkinter

Este projeto é um simulador de semáforo desenvolvido em Python utilizando a biblioteca Tkinter.
A aplicação reproduz três luzes (vermelho, amarelo e verde) e alterna automaticamente entre elas seguindo um ciclo configurado.
O usuário também pode iniciar, parar o ciclo e acionar o comando de pedestre, que reduz o tempo restante do sinal verde.

# Funcionalidades
-Ciclo automático

-Alternância entre vermelho, verde e amarelo.

-Tempo de cada fase configurável no código.

# Controles do usuário
-Start: Inicia o funcionamento do semáforo.

-Stop: Interrompe o ciclo e reseta as luzes-

-Pedestre: Reduz o tempo restante do verde para 1 segundo quando o pedido for feito durante essa fase.

# Interface gráfica
-Desenho das luzes em um Canvas.

-Exibição do estado atual e do tempo restante.

# Requisitos
-Python 3.x

-Tkinter (já incluído por padrão na maior parte das instalações do Python)

# Funcionamento Interno
O programa utiliza o método after() do Tkinter para criar uma contagem regressiva não bloqueante.
Cada fase do semáforo chama a próxima, mantendo um loop contínuo enquanto o programa estiver ativo.

### luxo simplificado:

1. O usuário pressiona Start.
2. O programa seleciona a primeira fase (vermelho).
3. A função countdown() controla o tempo e chama next_phase() ao final.
4. O ciclo se repete indefinidamente até o usuário pressionar Stop.
