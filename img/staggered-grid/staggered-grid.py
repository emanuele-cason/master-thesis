import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

def plot_staggered_configuration(velocity_type, filename):
    """
    velocity_type: 'u', 'v', o 'w'
    filename: nome del file di output
    """
    # Creazione della figura
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Parametri della griglia base
    nx, ny, nz = 2, 2, 2
    dx, dy, dz = 1.0, 1.0, 1.0

    # --- 1. Disegno della Griglia Standard (Grigia) ---
    grid_color = 'gray'
    grid_alpha = 0.5
    grid_lw = 1.5

    # Linee verticali (Z)
    for i in range(nx + 1):
        for j in range(ny + 1):
            ax.plot([i*dx, i*dx], [j*dy, j*dy], [0, nz*dz], color=grid_color, alpha=grid_alpha, linewidth=grid_lw)
    # Linee Y
    for i in range(nx + 1):
        for k in range(nz + 1):
            ax.plot([i*dx, i*dx], [0, ny*dy], [k*dz, k*dz], color=grid_color, alpha=grid_alpha, linewidth=grid_lw)
    # Linee X
    for j in range(ny + 1):
        for k in range(nz + 1):
            ax.plot([0, nx*dx], [j*dy, j*dy], [k*dz, k*dz], color=grid_color, alpha=grid_alpha, linewidth=grid_lw)

    # --- 2. Configurazione specifica per tipo di cella ---
    
    # Inizializziamo liste vuote
    u_nodes = []
    v_nodes = []
    w_nodes = []
    box_color = 'black'
    box_bounds = [] # [xmin, xmax, ymin, ymax, zmin, zmax]
    
    sphere_size_face = 100
    sphere_size_center = 180 # Nodo centrale più grande

    if velocity_type == 'u':
        # --- CONFIGURAZIONE U (BLU) ---
        box_color = 'blue'
        # Centro su un nodo u (faccia x)
        center = np.array([1.0 * dx, 0.5 * dy, 0.5 * dz])
        # Box u è shiftato in X di mezza cella
        box_bounds = [center[0]-dx/2, center[0]+dx/2, center[1]-dy/2, center[1]+dy/2, center[2]-dz/2, center[2]+dz/2]
        
        # Nodo centrale (u)
        u_nodes.append(center)
        
        # Nodi sulle facce (v e w)
        # v (verde) sulle facce y=0 e y=1 del box
        v_nodes = [
            [0.5*dx, 0.0*dy, 0.5*dz], [1.5*dx, 0.0*dy, 0.5*dz],
            [0.5*dx, 1.0*dy, 0.5*dz], [1.5*dx, 1.0*dy, 0.5*dz]
        ]
        # w (rosso) sulle facce z=0 e z=1 del box
        w_nodes = [
            [0.5*dx, 0.5*dy, 0.0*dz], [1.5*dx, 0.5*dy, 0.0*dz],
            [0.5*dx, 0.5*dy, 1.0*dz], [1.5*dx, 0.5*dy, 1.0*dz]
        ]

    elif velocity_type == 'v':
        # --- CONFIGURAZIONE V (VERDE) ---
        box_color = 'green'
        # Centro su un nodo v (faccia y)
        center = np.array([0.5 * dx, 1.0 * dy, 0.5 * dz])
        # Box v è shiftato in Y di mezza cella
        box_bounds = [center[0]-dx/2, center[0]+dx/2, center[1]-dy/2, center[1]+dy/2, center[2]-dz/2, center[2]+dz/2]
        
        # Nodo centrale (v)
        v_nodes.append(center)
        
        # Nodi sulle facce (u e w)
        # u (blu) sulle facce x=0 e x=1 del box (box x va da 0 a 1 qui)
        u_nodes = [
            [0.0*dx, 0.5*dy, 0.5*dz], [0.0*dx, 1.5*dy, 0.5*dz], # Faccia sinistra
            [1.0*dx, 0.5*dy, 0.5*dz], [1.0*dx, 1.5*dy, 0.5*dz]  # Faccia destra
        ]
        # w (rosso) sulle facce z=0 e z=1 del box
        w_nodes = [
            [0.5*dx, 0.5*dy, 0.0*dz], [0.5*dx, 1.5*dy, 0.0*dz],
            [0.5*dx, 0.5*dy, 1.0*dz], [0.5*dx, 1.5*dy, 1.0*dz]
        ]

    elif velocity_type == 'w':
        # --- CONFIGURAZIONE W (ROSSO) ---
        box_color = 'red'
        # Centro su un nodo w (faccia z)
        center = np.array([0.5 * dx, 0.5 * dy, 1.0 * dz])
        # Box w è shiftato in Z di mezza cella
        box_bounds = [center[0]-dx/2, center[0]+dx/2, center[1]-dy/2, center[1]+dy/2, center[2]-dz/2, center[2]+dz/2]
        
        # Nodo centrale (w)
        w_nodes.append(center)
        
        # Nodi sulle facce (u e v)
        # u (blu) sulle facce x=0 e x=1 del box
        u_nodes = [
            [0.0*dx, 0.5*dy, 0.5*dz], [0.0*dx, 0.5*dy, 1.5*dz],
            [1.0*dx, 0.5*dy, 0.5*dz], [1.0*dx, 0.5*dy, 1.5*dz]
        ]
        # v (verde) sulle facce y=0 e y=1 del box
        v_nodes = [
            [0.5*dx, 0.0*dy, 0.5*dz], [0.5*dx, 0.0*dy, 1.5*dz],
            [0.5*dx, 1.0*dy, 0.5*dz], [0.5*dx, 1.0*dy, 1.5*dz]
        ]

    # --- 3. Rendering ---
    
    # Plot del Box Tratteggiato
    def plot_box_edges(ax, bounds, style='--', color='blue'):
        xmin, xmax, ymin, ymax, zmin, zmax = bounds
        corners = [[xmin, ymin, zmin], [xmax, ymin, zmin], [xmax, ymax, zmin], [xmin, ymax, zmin],
                   [xmin, ymin, zmax], [xmax, ymin, zmax], [xmax, ymax, zmax], [xmin, ymax, zmax]]
        edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        for start, end in edges:
            p1, p2 = corners[start], corners[end]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], linestyle=style, color=color, linewidth=2.5)

    plot_box_edges(ax, box_bounds, style='--', color=box_color)

    # Plot delle palline
    # Converti in numpy array per facilità (se non vuoti)
    if u_nodes:
        u_nodes = np.array(u_nodes)
        # Se stiamo plottando la cella U, il nodo centrale è U, quindi è più grande
        s = sphere_size_center if velocity_type == 'u' else sphere_size_face
        edge = 'black' if velocity_type == 'u' else None
        ax.scatter(u_nodes[:,0], u_nodes[:,1], u_nodes[:,2], color='blue', s=s, edgecolors=edge, alpha=1.0)
    
    if v_nodes:
        v_nodes = np.array(v_nodes)
        s = sphere_size_center if velocity_type == 'v' else sphere_size_face
        edge = 'black' if velocity_type == 'v' else None
        ax.scatter(v_nodes[:,0], v_nodes[:,1], v_nodes[:,2], color='green', s=s, edgecolors=edge, alpha=1.0)

    if w_nodes:
        w_nodes = np.array(w_nodes)
        s = sphere_size_center if velocity_type == 'w' else sphere_size_face
        edge = 'black' if velocity_type == 'w' else None
        ax.scatter(w_nodes[:,0], w_nodes[:,1], w_nodes[:,2], color='red', s=s, edgecolors=edge, alpha=1.0)

    # Setup estetico
    font_size_axes = 20
    ax.set_xlabel('X', fontsize=font_size_axes, labelpad=10)
    ax.set_ylabel('Y', fontsize=font_size_axes, labelpad=10)
    ax.set_zlabel('Z', fontsize=font_size_axes, labelpad=10)
    
    # Limiti e aspetto
    ax.set_xlim(-0.2, 2.2)
    ax.set_ylim(-0.2, 2.2)
    ax.set_zlim(-0.2, 2.2)
    ax.set_box_aspect([1, 1, 1])
    
    # Pulizia
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Legenda Dinamica
    legend_elements = [
        Line2D([0], [0], color='blue', marker='o', markersize=10, lw=0, label='u velocity'),
        Line2D([0], [0], color='green', marker='o', markersize=10, lw=0, label='v velocity'),
        Line2D([0], [0], color='red', marker='o', markersize=10, lw=0, label='w velocity'),
        Line2D([0], [0], color=box_color, linestyle='--', lw=2, label=f'{velocity_type}-CV (Momentum)')
    ]
    #ax.legend(handles=legend_elements, loc='upper right', fontsize=12)

    # Vista
    ax.view_init(elev=25, azim=30)
    
    plt.tight_layout()
    print(f"Esportazione immagine: {filename}")
    plt.savefig(filename, dpi=300)
    plt.close() # Chiude la figura per liberare memoria

# Esecuzione per i 3 casi
if __name__ == "__main__":
    plot_staggered_configuration('u', 'staggered_cell_U_blue.jpg')
    plot_staggered_configuration('v', 'staggered_cell_V_green.jpg')
    plot_staggered_configuration('w', 'staggered_cell_W_red.jpg')