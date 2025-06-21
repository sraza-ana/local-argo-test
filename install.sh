kubectl create namespace argocd || true
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

echo "Waiting for ArgoCD to be ready..."
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=argocd-server -n argocd --timeout=300s

ARGOCD_PASSWORD=$(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)
echo "ArgoCD admin password: $ARGOCD_PASSWORD"

# Port forward
echo "Starting port-forward to ArgoCD UI..."
echo "Access ArgoCD at: https://localhost:8080"
echo "Username: admin"
echo "Password: $ARGOCD_PASSWORD"
kubectl port-forward svc/argocd-server -n argocd 8080:443